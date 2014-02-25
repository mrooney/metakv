metakv
======

metakv is a concept-SaaS key-value store which stores data in metakv. This both lacks meaning and accurately describes its implementation.

metakv is not ACID-compliant; particularly, the durability of any data stored in metakv is undefined.

how does it work?
=================

metakv uses GitHub issues on the metakv project itself as its data store / backend. You can obtain
an API token via GitHub OAuth at http://www.metakv.com, which will then provide
programmatic operations like GET and SET. Keys and values are base32
encoded and stored in GitHub issues (filed by you via OAuth) as issue titles and bodies,
respectively. Each user receives their own key space; issues are filed
and filtered by their username. They look like this: https://github.com/mrooney/metakv/issues

api
===
once you [obtain an access token](http://www.metakv.com), you'll be able
to:

* **GET**: curl http://www.metakv.com/get/:key?access_token=:token
* **SET**: curl -X POST -d '**:value**' http://www.metakv.com/set/:key?access_token=:token

why?
====

metakv was inspired by [@chino](https://github.com/chino), who first planted the idea of using
social data (tweets, facebook comments) outside of its original intent, and specifically as a place
to dump and retrieve raw encoded data. I loved the idea of a project
that could store its own data as metadata on the project itself. Hence,
metakv was born.

what's next?
============
maybe backends based on tweets to @metakv or comments on a metakv
Facebook page. maybe more operations like INCR, or data types like sets.
maybe nothing.
