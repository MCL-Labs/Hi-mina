"""FastAPI server for llama.cpp.

To run this example:

```bash
export MODEL=../models/7B/...
```

Then run:
```
uvicorn app:app --reload
```

or

```
python3 -m ./app.py
```

Then visit http://localhost:8000/docs to see the interactive Swagger API docs.

"""
import os
import argparse

import uvicorn

#from llama_cpp.server.app import create_app, Settings

if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # for name, field in Settings.__fields__.items():
    #     description = field.field_info.description
    #     if field.default is not None and description is not None:
    #         description += f" (default: {field.default})"
    #     parser.add_argument(
    #         f"--{name}",
    #         dest=name,
    #         type=field.type_,
    #         help=description,
    #     )

    # args = parser.parse_args()
    # settings = Settings(**{k: v for k, v in vars(args).items() if v is not None})
    # app = create_app(settings=settings)

    # uvicorn.run(
    #     app, host=os.getenv("HOST", "localhost"), port=int(os.getenv("PORT", 8000))
    # )
    pass