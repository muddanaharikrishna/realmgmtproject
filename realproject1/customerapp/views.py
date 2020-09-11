from django.shortcuts import render
from customerapp.models import Customer, Company, Blockname, Floors, Unit, Facing, UnitCreation, Amenities, UnitType, Scheme, UnitCosting
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def dashboard_View(request):
    return render(request,'customerapp/mydashboard.html')

class CustomerListView(ListView):
    model=Customer

class CustomerDetailView(DetailView):
    model=Customer

class CustomerCreateView(CreateView):
    model=Customer
    fields='__all__'

class CustomerUpdateView(UpdateView):
    model=Customer
    fields='__all__'

class CustomerDeleteView(DeleteView):
    model=Customer
    success_url=reverse_lazy('customers')

class CompanyListView(ListView):
    model=Company

class CompanyDetailView(DetailView):
    model=Company

class CompanyCreateView(CreateView):
    model=Company
    fields='__all__'

class CompanyUpdateView(UpdateView):
    model=Company
    fields='__all__'

class CompanyDeleteView(DeleteView):
    model=Company
    success_url=reverse_lazy('companies')

class BlockListView(ListView):
    model=Blockname

class BlockDetailView(DetailView):
    model=Blockname

class BlockCreateView(CreateView):
    model=Blockname
    fields='__all__'

class BlockUpdateView(UpdateView):
    model=Blockname
    fields='__all__'

class BlockDeleteView(DeleteView):
    model=Blockname
    success_url=reverse_lazy('blocknames')

class FloorsListView(ListView):
    model=Floors

class FloorsDetailView(DetailView):
    model=Floors

class FloorsCreateView(CreateView):
    model=Floors
    fields='__all__'

class FloorsUpdateView(UpdateView):
    model=Floors
    fields='__all__'

class FloorsDeleteView(DeleteView):
    model=Floors
    success_url=reverse_lazy('floornames')

class UnitListView(ListView):
    model=Unit

class UnitDetailView(DetailView):
    model=Unit

class UnitCreateView(CreateView):
    model=Unit
    fields='__all__'

class UnitUpdateView(UpdateView):
    model=Unit
    fields='__all__'

class UnitDeleteView(DeleteView):
    model=Unit
    success_url=reverse_lazy('units')

class FacingListView(ListView):
    model=Facing

class FacingDetailView(DetailView):
    model=Facing

class FacingCreateView(CreateView):
    model=Facing
    fields='__all__'

class FacingUpdateView(UpdateView):
    model=Facing
    fields='__all__'

class FacingDeleteView(DeleteView):
    model=Facing
    success_url=reverse_lazy('facings')

class UnitCreationListView(ListView):
    model=UnitCreation

class UnitCreationDetailView(DetailView):
    model=UnitCreation

class UnitCreationCreateView(CreateView):
    model=UnitCreation
    fields='__all__'

class UnitCreationUpdateView(UpdateView):
    model=UnitCreation
    fields='__all__'

class UnitCreationDeleteView(DeleteView):
    model=UnitCreation
    success_url=reverse_lazy('unitcreations')

class AmenitiesListView(ListView):
    model=Amenities

class AmenitiesDetailView(DetailView):
    model=Amenities

class AmenitiesCreateView(CreateView):
    model=Amenities
    fields='__all__'

class AmenitiesUpdateView(UpdateView):
    model=Amenities
    fields='__all__'

class AmenitiesDeleteView(DeleteView):
    model=Amenities
    success_url=reverse_lazy('amenities')

class UnitTypeListView(ListView):
    model=UnitType

class UnitTypeDetailView(DetailView):
    model=UnitType

class UnitTypeCreateView(CreateView):
    model=UnitType
    fields='__all__'

class UnitTypeUpdateView(UpdateView):
    model=UnitType
    fields='__all__'

class UnitTypeDeleteView(DeleteView):
    model=UnitType
    success_url=reverse_lazy('unittype')

class SchemeListView(ListView):
    model=Scheme

class SchemeDetailView(DetailView):
    model=Scheme

class SchemeCreateView(CreateView):
    model=Scheme
    fields='__all__'

class SchemeUpdateView(UpdateView):
    model=Scheme
    fields='__all__'

class SchemeDeleteView(DeleteView):
    model=Scheme
    success_url=reverse_lazy('scheme')

class UnitCostingListView(ListView):
    model=UnitCosting

class UnitCostingDetailView(DetailView):
    model=UnitCosting

class UnitCostingCreateView(CreateView):
    model=UnitCosting
    fields='__all__'

class UnitCostingUpdateView(UpdateView):
    model=UnitCosting
    fields='__all__'

class UnitCostingDeleteView(DeleteView):
    model=UnitCosting
    success_url=reverse_lazy('unitcosting')
