#!/bin/sh
#
# ---------------------------------------------------------------------
# PyCharm startup script.
# ---------------------------------------------------------------------
#

/opt/couchbase/bin/tools/cbdocloader -u naveay -p Xx56909752 -n 127.0.0.1:8091 -b TwitterUsers -s 100 TwitterUsers

/opt/couchbase/bin/tools/cbdocloader -u naveay -p Xx56909752 -n 127.0.0.1:8091 -b FacebookMessages -s 100 FacebookMessages

/opt/couchbase/bin/tools/cbdocloader -u naveay -p Xx56909752 -n 127.0.0.1:8091 -b FacebookUsers -s 100 FacebookUsers

/opt/couchbase/bin/tools/cbdocloader -u naveay -p Xx56909752 -n 127.0.0.1:8091 -b TweetMessages -s 100 TweetMessages

