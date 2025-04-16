import tiktoken

encoder = tiktoken.encoding_for_model('gpt-4o')

print("Vocab Size:", encoder.n_vocab) # Vocab Size: 200019


text = "Hello, world! This is a test."

tokens = encoder.encode(text)
print("Tokens:", tokens) # Tokens: [13225, 11, 2375, 0, 1328, 382, 261, 1746, 13]

my_tokens = [13225, 11, 2375, 0, 1328, 382, 261, 1746, 13]
decoded = encoder.decode(my_tokens)
print("Decoded:", decoded)  # Decoded: Hello, world! This is a test.
