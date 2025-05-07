import requests
from datetime import datetime

#https://stoppested.entur.org/?stopPlaceId=NSR:StopPlace:43577

url = "https://api.entur.io/journey-planner/v3/graphql"
query = """
{
  quay(id: "NSR:Quay:74792") {
    id
    name
    estimatedCalls(timeRange: 7200, numberOfDepartures: 10) {
      expectedArrivalTime
      destinationDisplay {
        frontText
      }
      serviceJourney {
        line {
          id
          name
        }
      }
    }
  }
}
"""

headers = {
    "Content-Type": "application/json",
    "ET-Client-Name": "your-app-name"
}

response = requests.post(url, json={'query': query}, headers=headers)
data = response.json()
#print(data)

quay = data['data']['quay']
print(f"Quay ID: {quay['id']}")
print(f"Quay Name: {quay['name']}")
print("\nEstimert ankomsttid og busstjenester:")

now = datetime.now()

for call in quay['estimatedCalls']:
    arrival_time_str = call['expectedArrivalTime']
    destination = call['destinationDisplay']['frontText']
    line_name = call['serviceJourney']['line']['name']
    
    # Konverter estimert ankomsttid til datetime-objekt
    arrival_time = datetime.fromisoformat(arrival_time_str[:-6])  # Fjern tidsforskjellen (timezone) før konvertering
    
    # Beregn differansen i minutter
    time_difference = (arrival_time - now).total_seconds() / 60
    
    print(f"\nAnkomsttid: {arrival_time_str}")
    print(f"Destinasjon: {destination}")
    print(f"Linje: {line_name}")
    print(f"Tid til ankomst: {time_difference:.2f} minutter")