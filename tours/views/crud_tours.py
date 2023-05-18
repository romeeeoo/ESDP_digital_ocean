from choices import StatusChoice
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from tours.forms.tour_create_form import TourCreateForm
from tours.models.tour import Tour


class TourListView(ListView):
    model = Tour
    context_object_name = 'tours'
    template_name = 'tour_list.html'

    def get_queryset(self):
        queryset = super(TourListView, self).get_queryset()
        return queryset.filter(moderation_status='CONFIRMED')


class TourCreateView(CreateView):
    template_name = 'tour_create.html'
    model = Tour
    form_class = TourCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.moderation_status = StatusChoice.SENT_TO_VERIFICATION
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tour_detail', kwargs={'pk': self.object.pk})


class TourDetailView(DetailView):
    template_name = 'tour_detail.html'
    model = Tour
    context_object_name = 'tour'


class TourUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'tour_update.html'
    model = Tour
    form_class = TourCreateForm

    def get_success_url(self):
        return reverse('tour_detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.get_object().author == self.request.user


class TourDeleteView(UserPassesTestMixin, DeleteView):
    model = Tour

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.author_id})

    def test_func(self):
        return self.get_object().author == self.request.user
