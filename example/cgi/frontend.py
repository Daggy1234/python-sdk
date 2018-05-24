#!/usr/bin/python
#################################################
# Example Implementation of LoginRadius Class   #
#################################################
# This is an example on how to use LoginRadius  #
# Python SDK                                    #
#################################################
# Copyright 2015-2016 LoginRadius Inc.          #
# - www.LoginRadius.com                         #
#################################################
# This file is part of the LoginRadius SDK      #
# package.                                      #
#################################################

#Your API Credentials
API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_SECRET_KEY"
CALLBACK_URL = "http://______________backend.py"


#Essential package for LoginRadius to communicate
from LoginRadius import LoginRadius as LR
LR.API_KEY = API_KEY
LR.API_SECRET = API_SECRET
#LR.LIBRARY ='urllib2'
login = LR()
#We need a request
sott = login.account.generateSott()
SOTT = sott.get('Sott')

#Print out our example Interface
print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Python Demo</title>')
print ('<link href="style.css" rel="stylesheet" type="text/css" media="all" />')
print ('<link href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css" rel="stylesheet" />')
print ('<script src="//code.jquery.com/jquery-2.2.1.min.js"></script>')
print ('<script src="//code.jquery.com/ui/1.12.1/jquery-ui.js"></script>')
print ('<script src="//auth.lrcontent.com/v2/js/LoginRadiusV2.js"></script>')
print ('<script type="text/javascript">var commonOptions = {};commonOptions.apiKey = "' + API_KEY +'";commonOptions.sott = "'+ SOTT +'";commonOptions.verificationUrl = window.location.origin+window.location.pathname;commonOptions.resetPasswordUrl = window.location.origin+window.location.pathname;commonOptions.formValidationMessage = true;commonOptions.hashTemplate = true;</script>')
print ('<script src="LoginRadiusFrontEnd.js"></script>')
print ('<script type="text/javascript">var ssologin_options= {};ssologin_options.onSuccess = function(response) {window.location="'+ CALLBACK_URL +'"};LRObject.util.ready(function() {LRObject.init("ssoLogin", ssologin_options);});</script>')
print ('</head>')
print ('<body>')
print ('<script type="text/html" id="loginradiuscustom_tmpl"><div class="lr-icon-box"><span class="lr-provider-label lr-sl-shaded-brick-button lr-flat-<#=Name.toLowerCase()#>" onclick="return  LRObject.util.openWindow(\'<#= Endpoint #>\');" title="<#= Name #>" alt="Sign in with <#=Name#>"><span class="lr-sl-icon lr-sl-icon-<#=Name.toLowerCase()#>"></span>Login with <#=Name#></span></div></script>')
print ('<div class="main-nav">')
print ('<div class="container">')
print ('<div class="logo-box">')
print ('<h1 class="logo">')
print ('LoginRadius')
print ('</h1>')
print ('<div class="site-description">python demo</div>')
print ('</div>')
print ('</div>')
print ('</div>')

print ('<div class="messages" style="display:none">')
print ('<ul>')
print ('<li class="messageinfo">')
print ('</li>')
print ('<div class="clear"></div>')
print ('</ul>')
print ('</div>')

print ('<div class="lr-frame lr-input-style">')
print ('<div class="lr-heading">Login with</div>')
print ('<div class="lr-login-buttons-frame lr-space-fix">')
print ('<div class="interfacecontainerdiv"></div>')
print ('</div>')
print ('<div id="lr-sign-in" class="lr-traditional-frame lr-pos-r lr-trad-login">')
print ('<div class="lr-heading lr-small lr-pos-a lr-or-bubble"><span>Or with email</span></div>')
print ('<div class="lr-form-frame lr-align-left">')
print ('<div id="login-container"></div>')
print ('<div class="lr-submit-frame lr-align-right">')
print ('<span class="lr-link-frame lr-pull-left">')
print ('<span class="lr-link lr-register" data-form="lr-register"><a>Register</a></span>')
print ('<span class="lr-link lr-forgot-pass" data-form="lr-forgot-pw"><a>Forgot Password?</a></span>')
print ('</span>')
print ('</div>')
print ('<div style="clear: both"></div>')
print ('</div>')
print ('</div>')

print ('<div id="lr-register" class="lr-traditional-frame lr-trad-register lr-pos-r">')
print ('<div class="lr-heading lr-small lr-pos-a lr-or-bubble"><span>Or create your account</span></div>')
print ('<div class="lr-form-frame lr-align-left">')
print ('<div id="registeration-container">')
print ('</div>')
print ('<div class="lr-submit-frame lr-align-right">')
print ('<span class="lr-link-frame lr-pull-left">')
print ('<span class="lr-link lr-sign-in" data-form="lr-sign-in"><a>Sign In</a></span>')
print ('<span class="lr-link lr-forgot-pass" data-form="lr-forgot-pw"><a>Forgot Password?</a></span>')
print ('</span>')
print ('</div>')
print ('<div style="clear: both"></div>')
print ('</div>')
print ('</div>')

print ('<div id="lr-social-register" class="lr-traditional-frame lr-social-register lr-pos-r">')
print ('<div class="lr-heading lr-small lr-pos-a lr-or-bubble"><span>Complete your profile to Register</span></div>')
print ('<div class="lr-form-frame lr-align-left">')
print ('<div id="social-registration-container">')
print ('</div>')
print ('<div class="lr-submit-frame lr-align-right">')
print ('<span class="lr-link-frame lr-pull-left">')
print ('<span class="lr-link lr-sign-in" data-form="lr-sign-in"><a>Sign In</a></span>')
print ('<span class="lr-link lr-forgot-pass" data-form="lr-forgot-pw"><a>Forgot Password?</a></span>')
print ('</span>')
print ('</div>')
print ('<div style="clear: both"></div>')
print ('</div>')
print ('</div>')

print ('<div id="lr-forgot-pw" class="lr-traditional-frame lr-pos-r lr-trad-forgot-pw">')
print ('<div class="lr-heading lr-small lr-pos-a lr-or-bubble"><span>Forgot Password</span></div>')
print ('<div class="lr-form-frame lr-align-left">')
print ('<div id="forgotpassword-container">')
print ('</div>')
print ('<div class="lr-submit-frame lr-align-right">')
print ('<span class="lr-link-frame lr-pull-left">')
print ('<span class="lr-link lr-sign-in" data-form="lr-sign-in"><a>Sign In</a></span>')
print ('<span class="lr-link lr-register" data-form="lr-register"><a>Register</a></span>')
print ('</span>')
print ('</div>')
print ('<div style="clear: both"></div>')
print ('</div>')
print (' </div>')
print (' <div id="lr-reset-pw" class="lr-traditional-frame lr-pos-r lr-trad-reset-pw">')
print (' <div class="lr-heading lr-small lr-pos-a lr-or-bubble"><span>Reset Password</span></div>')
print (' <div class="lr-form-frame lr-align-left">')
print (' <div id="resetpassword-container">')
print ('</div>')
print ('<div class="lr-submit-frame lr-align-right">')
print ('<span class="lr-link-frame lr-pull-left">')
print ('<span class="lr-link lr-sign-in" data-form="lr-sign-in"><a>Sign In</a></span>')
print ('<span class="lr-link lr-register" data-form="lr-register"><a>Register</a></span>')
print ('</span>')
print ('</div>')
print ('<div style="clear: both"></div>')
print ('</div>')
print ('</div>')
print ('</div>')
print ('</body>')
print ('</html>')
