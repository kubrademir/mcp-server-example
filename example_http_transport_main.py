from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mcp_server import mcp as docs_mcp_server
import contextlib
import uvicorn

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
  async with contextlib.AsyncExitStack() as stack:
    await stack.enter_async_context(docs_mcp_server.session_manager.run())
    yield

app = FastAPI(lifespan=lifespan)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for simplicity
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

app.mount("/docs", docs_mcp_server.streamable_http_app())


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080, log_level="debug")    