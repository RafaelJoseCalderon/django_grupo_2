from .utils import messages_success


class MessagesSuccessMixin:
    messages_success = None

    def form_valid(self, form):
        if messages_success:
            messages_success(self.request, self.messages_success)

        return super().form_valid(form)
