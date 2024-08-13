from django.http import HttpResponseForbidden

class RequestForbiddenMiddleware:
      def process_view(self,request,view_func, view_args,view_kwargs):
          if request.path == '/sensitive_content':
                return HttpResponseForbidden('/home')
          return None
