import datetime
import collections
import logging
import itertools
from optparse import OptionParser

from libsaas.services import ducksboard, zendesk


logging.basicConfig(level=logging.WARNING)


def create_parser():
    parser = OptionParser()
    parser.add_option("-u", "--username")
    parser.add_option("-p", "--password")
    parser.add_option("-d", "--domain")
    parser.add_option("-a", "--api-key")
    parser.add_option("-l", "--label")
    parser.add_option("-x", "--days-ago", type=int, default=7)
    parser.add_option("-v", "--verbose", action='store_true')

    return parser


def get_tickets(zservice, days_ago):
    ago = datetime.datetime.now() - datetime.timedelta(days=days_ago)
    q = 'status>=solved updated>%s type:ticket' % ago.strftime('%Y-%m-%d')

    tickets = []
    for page in itertools.count(1):
        batch = zservice.search(q, 'desc', 'updated_at', page=page, per_page=50)
        tickets.extend(batch['results'])
        if len(batch['results']) < 50:
            break

    return tickets


def make_board(zservice, tickets):
    c = collections.Counter([t['assignee_id'] for t in tickets])
    items = []
    for user_id, count in c.most_common(11):
        user = zservice.user(user_id).get()['user']
        items.append({'name': user['name'], 'values': [count]})

    return {'board': items}


def main():
    parser = create_parser()

    opts, args = parser.parse_args()
    if opts.verbose:
        logging.getLogger('libsaas').setLevel(logging.DEBUG)

    zservice = zendesk.Zendesk(opts.domain, opts.username, opts.password)
    dservice = ducksboard.Ducksboard(opts.api_key)

    tickets = get_tickets(zservice, opts.days_ago)
    board = make_board(zservice, tickets)
    dservice.data_source(opts.label).push({'value': board})


if __name__ == '__main__':
    main()
