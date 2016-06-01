from django.core.paginator import Paginator

def paginate(objects, request, reqPage=None, perPage=None):
    """
    @param objects (list)
    @return dict
    """
    try:
        request_page = int(request.GET.get('page'))
    except:
        request_page = 1

    # pagination
    last_page = 1
    hasNext = None
    hasPrevious = None
    length = len(objects)
    per_page=50
    pagination = Paginator(objects, per_page)

    last_page = pagination.num_pages
    if last_page >= request_page:
        objects = pagination.page(request_page).object_list
    # pageout
    else:
        request_page = 1
        objects = pagination.page(request_page).object_list
    hasNext = pagination.page(request_page).has_next()
    hasPrevious = pagination.page(request_page).has_previous()
     
    response = {}
    response['data'] = objects
    response['last_page'] = last_page
    response['request_page'] = int(request_page)
    response['hasNext'] = hasNext
    response['hasPrevious'] = hasPrevious
    response['length'] = length
    return response

