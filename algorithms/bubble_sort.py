def bubble_sort(arr, draw_bars_callback):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            # Pass the index of the bar being compared
            draw_bars_callback(arr, compared_index=j)  # Highlight the bar at index j
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            draw_bars_callback(arr)  # Redraw bars without highlighting
