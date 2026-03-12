from ais_bench.benchmark.models import VLLMCustomAPIChat
from ais_bench.benchmark.utils.postprocess.model_postprocessors import extract_non_reasoning_content

models = [
    dict(
        attr="service",
        type=VLLMCustomAPIChat,
        abbr="vllm-multiturn-api-chat-stream",
        path="/root/autodl-tmp/models/Qwen3-8B",
        model="qwen3_8b",
        stream=True,
        request_rate=0,
        retry=2,
        api_key="",
        host_ip="127.0.0.1",
        host_port=8000,
        url="",
        max_out_len=512,
        batch_size=30,
        trust_remote_code=False,
        generation_kwargs=dict(
            temperature=0.01,
            ignore_eos=False,
        ),
        pred_postprocessor=dict(type=extract_non_reasoning_content),
    )
]

