def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    
    return _find_peak_helper(list_of_integers, 0, len(list_of_integers) - 1)

def _find_peak_helper(arr, low, high):
    mid = (low + high) // 2
    
    # Check if the middle element is a peak
    if (mid == 0 or arr[mid] >= arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] >= arr[mid + 1]):
        return arr[mid]
    
    # If the left neighbor is greater, then the peak is in the left half
    elif mid > 0 and arr[mid - 1] > arr[mid]:
        return _find_peak_helper(arr, low, mid - 1)
    
    # If the right neighbor is greater, then the peak is in the right half
    else:
        return _find_peak_helper(arr, mid + 1, high)

