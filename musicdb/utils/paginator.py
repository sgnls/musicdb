from django.core.paginator import Paginator, EmptyPage, Page

class AutoPaginator(Paginator):
    def __init__(self, request, *args, **kwargs):
        self.request = request
        self.default = kwargs.pop('default', 1)
        super(AutoPaginator, self).__init__(*args, **kwargs)

    def current_page(self):
        try:
            page = int(self.request.GET['page'])

            if page <= 0:
                raise ValueError()
        except (ValueError, KeyError):
            page = self.default

        try:
            return self.page(page)
        except EmptyPage:
            return Page([], page, self)

    def validate_number(self, number):
        """
        Our version ignores EmptyPage.
        """
        try:
            return max(1, int(number))
        except (TypeError, ValueError):
            return 1

def range_skip_list(pages):
    out = [(pages[0], pages[0])]

    for x in pages[1:]:
        if out[-1][1] == x - 1:
            out[-1] = (out[-1][0], x)
        else:
            out.append((x, x))
    return out
