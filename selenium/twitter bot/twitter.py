import requests

twitter_endpoit = "https://api.twitter.com/2/tweets/counts/all"
twitter_id = "aditya13920"
twitter_username = "adityakumar5544332211@gmail.com"
twitter_pass = "kumaraditya1392"
twitter_client_id = "QjV4UVl3VTJnZkhZUUFNc1c0blk6MTpjaQ"
twitter_client_secret_id = "aHIypPege0nNv2eehq0Ai0iQiVoDyVPcr2nuKeasEJxS9UtE0z"
twitter_bearer_code = "AAAAAAAAAAAAAAAAAAAAADn5gwEAAAAAyI826hICDvV5pe6qP%2FflC9upgkM%3DbnjPpmWfM2oIqCfFBdM6ApryBGjH0gzfPn2dxV5v0w2HjKCGZJ"

response = requests.get(twitter_endpoit)
print(response.status_code)
print(response.text)