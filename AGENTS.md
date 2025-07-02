> **IMPORTANT:**  
> Your output **must** be exactly one JSON object invoking the `git_apply_patch` tool.  
> No other text or code. For example:
>
> ```json
> {
>   "name": "git_apply_patch",
>   "arguments": {
>     "patch": "diff --git a/foo.py b/foo.py\nindex 123..456 100644\n--- a/foo.py\n+++ b/foo.py\n@@ -1,4 +1,4 @@\n- old line\n+ new line\n"
>   }
> }
> ```
>
> If you include any pseudocode or free-form text, it will cause a failure.
