curl -X 'POST' \
  'https://be7c-222-172-244-12.ngrok-free.app/v1/chat/completions' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer sk-afwawfwadawfa' \
  -d '{
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "What is the capital of France?"
    }
  ],
  "max_tokens": 1024,
  "stream": false
}'

curl -X 'POST' \
  'https://be7c-222-172-244-12.ngrok-free.app/v1/chat/completions' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer my_api_key' \
  -d '{
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "What is the capital of France?"
    }
  ],
  "max_tokens": 1024,
  "stream": false
}'