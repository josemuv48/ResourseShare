from django.conf import settings
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin
from apps.core.logging import Logging
import logging

#logging = Logging(str(settings.BASE_DIR/'logs'/'req_res_logs.txt'))

logger = logging.getLogger('logging-old')


def simple_logging_middleware(get_response):
    
    def middleware(request):
        #pre-processing
        http_method = request.method
        url = request.get_full_path()
        host_port = request.get_host()
        content_type = request.headers['Content-Type']
        user_agent = request.headers['User-Agent']
        msg = f'{http_method} | {host_port}{url} | {content_type} | {user_agent}'
        logging.info(msg)
        
        secure = request.is_secure()
        if secure == False:
            msg = f'{http_method} | {host_port}{url} | {content_type} | IS_SECURE: {secure}'
            logging.warning(msg)
        
        response = get_response(request)
        headers = response.headers
        msg = f'{headers}'
        logging.warning(msg)
        
        #post-processing

        # TODO: Investigate the response and decide on what to log
        # TODO: Formulate your message
        # TODO: log using the info level method

        return response
    
    return middleware



class ViewExecutionTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        # Pre-processing
        # START TIMER
        start_time = timezone.now()
        
        response = self.get_response(request)
        
        #Post - Processing
        # STOP TIMER
        total_time = timezone.now() - start_time
        http_method = request.method
        url = request.get_full_path()
        host_port = request.get_host()
        # msg = [INFO]/[WARNING]/[CRITICAL] EXECUTION TIME {total_time} >> {http_method} | {host_port}{url}
        
        msg = f"EXECUTION TIME {total_time} >> {http_method} | {host_port}{url}"
        logging.warning(msg)
        return response

   
class ViewExecutionTime2Middleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = timezone.now()
        
    def process_response(self, request, response):    
        total_time = timezone.now() - request.start_time
        http_method = request.method
        url = request.get_full_path()
        host_port = request.get_host()

        msg = f"EXECUTION TIME {total_time} >> {http_method} | {host_port}{url}"
        logging.critical(msg)

        return response 
    
    
    
    
    
    
# skeleton for custom Middleware 
''' 
class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request: HttpRequest, *args, **kwargs):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_view(self, request: HttpRequest, view_func, view_args, view_kwargs) -> None | HttpResponse:
        """
        # Is called just before Django calls the view
        NOTE: Accessing request.POST inside middleware before the view runs or in process_view()
        will prevent any view running after the middleware from being able to modify the upload
        handlers for the request, and should normally be avoided.
        """
        return None

    def process_exception(self, request: HttpRequest, exception: Exception) -> None | HttpResponse:
        """
        Django calls process_exception() when a view raises an exception.
        process_exception() should return either None or an HttpResponse object.
        If it returns an HttpResponse object, the template response and response middleware will be applied and
        the resulting response returned to the browser. Otherwise, default exception handling kicks in.
        """
        return None

    def process_template_response(self, request: HttpRequest, response: TemplateResponse):
        """
        request is an HttpRequest object. response is the TemplateResponse object
        (or equivalent) returned by a Django view or by a middleware.
        process_template_response() is called just after the view has finished executing,
        if the response instance has a render() method, indicating that it is a TemplateResponse or equivalent.
        It mmust return a response object that implements a render method. It could alter the given response by changing
        response.template_name and response.context_data, or it could create and return a brand-new TemplateResponse
        or equivalent.
        """
        return response
        
'''