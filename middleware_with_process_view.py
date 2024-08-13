class LoginUserIDMiddleware:
      def process_view(self, request,view_func,view_args,view_kwargs):
          if 'user_id' in view_kwargs:
              user_id = view_kwargs['user_id']
              print(f"Your UserID is {user_id}")
              return None
            

online = LoginUserIDMiddleware
online.process_view(1,2,3,4,{'user_id': 897654334})
