#!/usr/bin/env python
import sys
from twython import Twython

CONSUMER_KEY = '0bVzq7nfOYBd061IbgHwjYWyy'
CONSUMER_SECRET = 'krxt7tmb1qZtZF8H1yEEnwvjlqgjgIfR0B3pDwILXBinpWYx5o'
ACCESS_KEY = '2961482583-dplTTmQpwk72JO2FAqeKiKlMtw0DRDqDJgXEXqd'
ACCESS_SECRET = 'idE222rHbVSAwbdq9OY5Qj6rbhQomhXnpaaqBfhes2wvV'

api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

api.update_status(status=sys.argv[1])
