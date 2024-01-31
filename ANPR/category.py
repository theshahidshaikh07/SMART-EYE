import cv2

# Load cascade files for two-wheeler, car, bus, and truck
two_wheeler_cascade = cv2.CascadeClassifier('two_wheeler.xml')
car_cascade = cv2.CascadeClassifier('car.xml')

# Define function to detect vehicle type and draw bounding box around it
import cv2

# Load cascade files for two-wheeler, car, bus, and truck
two_wheeler_cascade = cv2.CascadeClassifier('two_wheeler.xml')
car_cascade = cv2.CascadeClassifier('car.xml')
bus_cascade = cv2.CascadeClassifier('Bus_front.xml')
truck_cascade = cv2.CascadeClassifier('Bus_front.xml')

# Define counts for two-wheelers and cars
two_wheeler_count = 0
car_count = 0
bus_count = 0
truck_count = 0

# Define function to detect vehicle type and draw bounding box around it
def detect_vehicle(frame, line_position):
    global two_wheeler_count, car_count, bus_count, truck_count # Use global variables for vehicle counts
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Draw margin line at the bottom of the frame
    margin = 50
    cv2.line(frame, (0, frame.shape[0] - margin), (frame.shape[1], frame.shape[0] - margin), (0, 255, 255), 2)

    # Detect two-wheelers
    two_wheelers = two_wheeler_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in two_wheelers:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, 'Two-Wheeler', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        # Check if two-wheeler crosses the margin line
        if y + h > frame.shape[0] - margin:
            two_wheeler_count += 1

    # Detect cars
    cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, 'Car', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        # Check if car crosses the margin line
        if y + h > frame.shape[0] - margin:
            car_count += 1

    buses = bus_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in buses:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, 'Bus', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        # Check if bus crosses the margin line
        if y + h > frame.shape[0] - margin:
            bus_count += 1

    trucks = truck_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in trucks:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, '=Truck', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        # Check if Truck crosses the margin line
        if y + h > frame.shape[0] - margin:
            truck_count += 1

    # Display vehicle counts above margin line
    cv2.putText(frame, f"Two-Wheeler count: {two_wheeler_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    cv2.putText(frame, f"Car count: {car_count}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    cv2.putText(frame, f"Bus count: {bus_count}", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    cv2.putText(frame, f"Truck count: {truck_count}", (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)


    # Display total vehicle count at top corner of the frame
    total_count = two_wheeler_count + car_count + truck_count + bus_count
    cv2.putText(frame, f"Total count: {total_count}", (10, 190), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    return frame




# Open video capture device
cap = cv2.VideoCapture('bikes.mp4')

line_position=300

# Loop through video frames
while True:
    # Read frame from video
    ret, frame = cap.read()

    # Check if frame was read successfully
    if not ret:
        break

    # Detect vehicle type and draw bounding box around it
    result_frame = detect_vehicle(frame, line_position)

    # Display result
    cv2.imshow('Video', result_frame)

    # Wait for key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture device and close all windows
cap.release()
cv2.destroyAllWindows()
