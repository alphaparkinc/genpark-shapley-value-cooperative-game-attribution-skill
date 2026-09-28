"""MCP stdio server for Shapley Value Attribution."""
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import ShapleyAttribution

def handle_rpc(request):
    req_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "compute_shapley",
                        "description": "Compute Shapley values given players and coalition values lookup",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "players": {"type": "array", "items": {"type": "string"}},
                                "coalition_values": {
                                    "type": "object",
                                    "description": "Map from comma-separated sorted players to float value, e.g. {'A': 10, 'A,B': 40}"
                                }
                            },
                            "required": ["players", "coalition_values"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "compute_shapley":
            players = args.get("players", [])
            val_map = args.get("coalition_values", {})
            def v_func(coalition):
                key = ",".join(sorted(coalition))
                return float(val_map.get(key, 0.0))
            res = ShapleyAttribution.compute_shapley_values(players, v_func)
            return {"jsonrpc": "2.0", "id": req_id, "result": res}
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method {name} not found"}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32600, "message": "Invalid request"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_rpc(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32700, "message": str(e)}}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
