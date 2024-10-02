# movies/views.py

import csv
import io
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Moviescontent
from datetime import datetime
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .serializers import MovieSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MovieFilter
from rest_framework.filters import OrderingFilter

@api_view(['POST'])  # Ensure this only allows POST requests
def upload_csv(request):
    if request.method == 'POST':
        print("Request method:", request.method)
        file_obj = request.FILES.get('file')
        if not file_obj or not file_obj.name.endswith('.csv'):
            return JsonResponse({'error': 'File is not CSV type'}, status=400)

    # Read the CSV file
    try:
        decoded_file = file_obj.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        csv_reader = csv.reader(io_string, delimiter=',')
        header = next(csv_reader)  # Skip the header row

        for row in csv_reader:
            try:
                # Convert budget, revenue, and vote_count to integer, if possible
                budget = int(float(row[0])) if row[0] else None
                revenue = int(float(row[6])) if row[6] else None
                vote_count = int(float(row[11])) if row[11] else None
                print(budget)

                # Validate and convert release_date to a valid date or None
                try:
                    release_date = datetime.strptime(row[5], '%Y-%m-%d').date() if row[5] else None
                except ValueError:
                    return JsonResponse({'error': f'Invalid date format in row: {row[5]}. Expected YYYY-MM-DD format.'}, status=400)

                # Create a Movie instance and save it
                _, created = Moviescontent.objects.get_or_create(
                    budget=budget,
                    homepage=row[1],
                    original_language=row[2],
                    original_title=row[3],
                    overview=row[4],
                    release_date=release_date,  # Use the validated date
                    revenue=revenue,
                    runtime=row[7],
                    status=row[8],
                    title=row[9],
                    vote_average=row[10],
                    vote_count=vote_count,
                    production_company_id=row[12],
                    genre_id=row[13],
                    languages=row[14],
                )
            except Exception as e:
                return JsonResponse({'error': f'Error processing row: {str(e)}'}, status=500)

        return JsonResponse({'message': 'CSV file uploaded successfully'}, status=201)

    except Exception as e:
        return JsonResponse({'error': f'File processing error: {str(e)}'}, status=500)

class MoviePagination(PageNumberPagination):
    page_size = 50  # Set the number of items per page
    page_size_query_param = 'page_size'  # Allow the client to set the page size
    max_page_size = 100  # Maximum number of items per page

class MovieListView(generics.ListAPIView):
    queryset = Moviescontent.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MoviePagination  # Apply pagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]  # Add filtering and ordering backends
    filterset_class = MovieFilter  # Use the MovieFilter for filtering
    ordering_fields = ['release_date', 'vote_average']  # Allow sorting by release_date and vote_average

