from rest_framework.views import exception_handler
from rest_framework import status
from django.http import Http404


def custom_exception_handler(exc, context):
    """
    This function will handle errors that are returned by
    the different views.
    The `handlers` dictionary will map
    each exception name to the function that should handle it.
    Each function should return a response with a message
    and the actual error.
    """

    # We Call REST framework's default exception handler first
    
    response = exception_handler(exc, context)
    handlers = {
        'ValidationError': _handle_generic_error,
        'Http404': _handle_generic_error,
        'PermissionDenied': _handle_generic_error,
        'NotAuthenticated': _handle_authentication_error
    }

    exception_class = exc.__class__.__name__

    if response is not None:
        response = _handle_generic_error(exc, context, response)

        if "AuthUserAPIView" in str(context['view']) and response.status_code == 401:
            response.status_code = status.HTTP_200_OK
            response.data = {'is_logged_in': False}
            return response

    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)

    return response


def _handle_generic_error(exc, context, response):
    return response


def _handle_authentication_error(exc, context, response):

    """If users are not logged in, we return this custom response"""
    response.data = {
        'error': 'Please log in to proceed.'
    }

    return response
