'''
@author:    xiaowing
@license:   Apache Lincese 2.0 
'''

from flask import request, redirect, make_response
from app.sso import SSO_Page
import app.SsoEntity.SsoToken as Token

class Login_Page():
    AUTH_CONST = { 'xiaowing':'asdf1234', 'postgres':'post1234'}

    @classmethod
    def login_clicked(cls, username, password):
        if not isinstance(username, str):
            raise TypeError("username not string.")

        if not isinstance(password, str):
            raise TypeError("password not string")

        '''if not isinstance(remember, bool):
            raise TypeError("remember_me not boolean.")'''
        if not Login_Page.validate_login(username, password):
            raise ValueError("The username or the password is incorrect.")

        token = Token.SSOToken(username)
        Token.SSOToken.SSOTokenList.append(token)
        #token.AddNewTicket()

        cookie_value = SSO_Page.SecurityValidationKey + SSO_Page.AuthTktUserdataDelimiter + token.ID

        returnUrl = request.args.get('returnUrl', '')
        if not returnUrl.strip():
            returnUrl = '/default'

        resp = make_response(redirect(returnUrl))
        resp.set_cookie(SSO_Page.FormsAuthCookieName, cookie_value)

        return resp


    # TODO: The following method needs to be rewritten with a database
    @classmethod
    def validate_login(cls, username, password):
        if username in Login_Page.AUTH_CONST:
            if Login_Page.AUTH_CONST[username] == password:
                return True
        return False


