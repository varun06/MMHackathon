#!/usr/bin/env python
#
# Copyright Varun Kumar

import os
import webapp2
import re
import jinja2

from session.views import *
from blog.views import *

PAGE_RE = r'(/(?:[a-zA-Z0-9_-]+/?)*)'

app = webapp2.WSGIApplication([('/',                        MainHandler),
                               ('/blog/signup',             SignupHandler),
                               ('/blog/login',              LoginHandler),
                               ('/blog/logout',             LogoutHandler),
                               ('/blog/welcome',            WelcomeHandler),
                               ('/blog',                    BlogHandler),
                               ('/blog/.json',              JSONBlogHandler),
                               ('/blog.json',               JSONBlogHandler),
                               ('/blog/newpost',            NewPostHandler),
                               ('/blog/(\d+)',              PostHandler),
                               ('/blog/(\d+)/.json',        JSONPostHandler),
                               ('/blog/(\d+).json',         JSONPostHandler),
                               ('/blog/flush',              FlushHandler)],
                              debug=True)