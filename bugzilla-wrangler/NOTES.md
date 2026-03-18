

**todo**

- Site Reports Resolution: --- Product: Web Compatibility - high value data we should optionally encorporate? Relavent bugs should get picked up in the crawl. 
    Lets make sure that's happening.
- Themes - from here, how do we dive deeper?

**Good Suggestions from Claude**

- Add a socorro-cli --facet platform step when a crash signature is found to better characterize Windows vs Linux vs macOS distribution.
- The --date range comparison for crash trends didn't return results for older windows when the signature is newly emerging — could detect "new signature" vs "rising trend" as distinct signal categories.
- Consider automatically fetching the cc_count field via a targeted follow-up request when it is missing from the initial batch response.
- The Graphics Triage Tracker meta (1632611) is a goldmine — consider fetching its 20 most-recently-changed deps as a standard step for the graphics scope.
- The cc_count field is systematically absent from Bugzilla REST API responses without authentication. The skill should document this more explicitly and suggest that comment_count is an acceptable substitute, or note that cc_count requires a logged-in API token to appear.