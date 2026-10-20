from pathlib import Path
import sys,json,copy
root=Path(sys.argv[1]);sys.path.insert(0,str(root/'packages/arcreel-market-core/src'))
from arcreel_market_core.endpoint_definition import validate_definition,render_request,build_context
folder=Path(__file__).resolve().parent
count=0
for f in folder.glob('arcreel-gpt*.json'):
 d=json.loads(f.read_text(encoding='utf-8'));result=validate_definition(d)
 assert result.valid,[(e.code,e.params) for e in result.errors]
 context=build_context({'base_url':'https://toapis.com','api_key':'local-test-placeholder','prompt':'a "quoted" prompt','model':'ignored-fixed-model','task_id':'test-task'},media_type='image')
 request=render_request(d['submit'],context,auth=d['auth']);assert request.url=='https://toapis.com/v1/images/generations'
 assert request.body['prompt']=='a "quoted" prompt' and request.headers['Authorization']=='Bearer local-test-placeholder'
 query=render_request(d['poll'],context,auth=d['auth']);assert query.url.endswith('/v1/images/generations/test-task')
 broken=copy.deepcopy(d);broken['submit']['body']['api_key']='{{ api_key }}';assert not validate_definition(broken).valid
 count+=1
assert count==3
print(json.dumps({'project':'ArcReel','upstream_validator':'passed','definitions':count,'request_render_checks':6,'negative_checks':3,'paid_calls':0,'full_ui_verified':False}))
