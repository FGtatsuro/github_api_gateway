import json
import sys

query = dict()
q = '''\
query schema {
  __type(name: "Repository") {
    name
    kind
    description
    fields {
      name
    }
  }
}

query repos($number_of_repos: Int!) {
  viewer {
    name
    repositories(last: $number_of_repos) {
      nodes {
        name
        forkCount
      }
    }
  }
}

query limitInfo {
  rateLimit {
    limit
    remaining
    resetAt
  }
}

query issues {
  viewer {
    repositories(first: 10) {
      edges {
        cursor
        node {
          name
          issues(first: 10, filterBy: {states: OPEN} ) {
            edges {
              cursor
              node {
                id
                url
                title
              }
            }
            pageInfo {
              ...pageInfoFields
            }
          }
        }
      }
      pageInfo {
        ...pageInfoFields
      }
    }
  }
}

fragment pageInfoFields on PageInfo {
  startCursor
  endCursor
  hasPreviousPage
  hasNextPage
}
'''

v = {
    "number_of_repos": 3
}


query['query'] = q
query['variables'] = v
select = 'schema'
if len(sys.argv) == 2:
    select = sys.argv[1]
query['operationName'] = select
sys.stdout.write(json.dumps(query))
