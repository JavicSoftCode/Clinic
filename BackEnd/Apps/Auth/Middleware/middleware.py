class NoCacheMiddleware:
  def __init__(self, get_response):
    self.get_response = get_response

  def __call__(self, request):
    response = self.get_response(request)
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response
#
# class NoCacheMiddleware:
#   def __init__(self, get_response):
#     self.get_response = get_response
#
#   def __call__(self, request):
#     # Obtener la respuesta
#     response = self.get_response(request)
#
#     # Aplicar encabezados para evitar que el navegador almacene en caché
#     response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
#     response['Pragma'] = 'no-cache'
#     response['Expires'] = '0'
#
#     return response
