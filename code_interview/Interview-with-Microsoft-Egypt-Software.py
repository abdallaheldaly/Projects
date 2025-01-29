#I had an interview with Microsoft Egypt on Monday, September 23, 2024, from 12 PM to 1 PM. 
# The article provided contained specific words and characters, 
# and we were asked to create a program that works with these characters and symbols only. 
# I considered using base64 encoding, but it included numbers and characters that were not required for the program. 
# The solution needed to focus only on the characters and symbols present in the article.


#////////////////////////////////////////////////////////////////////////////////////////////

# article
# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc ornare mollis felis, 
# nec imperdiet mi. Nulla ultricies nisi sit amet convallis porta. Nullam vitae lectus ullamcorper, 
# interdum ligula a, vestibulum est. Pellentesque in pharetra mauris. Nunc vehicula pellentesque elit, 
# vestibulum fermentum metus facilisis ac. Phasellus vitae ligula facilisis, lacinia ligula quis, 
# pellentesque nunc. Vivamus eget metus vel ante fermentum rutrum vel ac magna. Donec at dignissim risus, 
# et aliquet odio. Morbi non laoreet nibh. Aenean elit ex, convallis eu arcu eu, sagittis pretium lacus. 
# Vivamus nec lobortis mi. Sed feugiat, nisl in euismod dictum, ligula dolor vehicula elit, 
# et congue turpis leo quis diam. Suspendisse luctus auctor leo, id rutrum turpis rhoncus id.

# binary data to string 64 bit


# Original article
article = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc ornare mollis felis, nec imperdiet mi. Nulla ultricies nisi sit amet convallis porta. Nullam vitae lectus ullamcorper, interdum ligula a, vestibulum est. Pellentesque in pharetra mauris. Nunc vehicula pellentesque elit, vestibulum fermentum metus facilisis ac. Phasellus vitae ligula facilisis, lacinia ligula quis, pellentesque nunc. Vivamus eget metus vel ante fermentum rutrum vel ac magna. Donec at dignissim risus, et aliquet odio. Morbi non laoreet nibh. Aenean elit ex, convallis eu arcu eu, sagittis pretium lacus. Vivamus nec lobortis mi. Sed feugiat, nisl in euismod dictum, ligula dolor vehicula elit, et congue turpis leo quis diam. Suspendisse luctus auctor leo, id rutrum turpis rhoncus id.
"""

# Allowed characters (letters, commas, periods, and spaces)
allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ., "

# Filter the article to include only the allowed characters
filtered_text = ''.join([char for char in article if char in allowed_chars])

print(f"Filtered text: {filtered_text}")



#////////////////////////////////////////////////////////////////////////////////////////


# # Define the allowed characters (based on article, commas, periods, and spaces)
# allowed_chars = (
#     "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ., "
# )

# # Create a mapping to index from 0 to len(allowed_chars)-1
# char_map = {i: allowed_chars[i] for i in range(len(allowed_chars))}

# # Function to encode binary data into the custom string
# def binary_to_custom_string(binary_data):
#     # Convert binary data to integer
#     int_data = int.from_bytes(binary_data, byteorder='big')

#     # Build the encoded string by mapping the integer to our character set
#     encoded_string = ''
#     while int_data > 0:
#         encoded_string = char_map[int_data % len(allowed_chars)] + encoded_string
#         int_data //= len(allowed_chars)

#     return encoded_string

# # Example binary data
# binary_data = b"Hello, World!"

# # Encode binary data
# encoded_string = binary_to_custom_string(binary_data)

# print(f"Encoded string: {encoded_string}")
