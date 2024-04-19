import uvicorn

from fastapi import APIRouter, FastAPI

from lib.model import RunParams


app = FastAPI()


@app.post("/api/compute")
def run_mdkp(data: RunParams) -> dict:
    return {
        "result": "not implemented yet"
    }


def main():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
