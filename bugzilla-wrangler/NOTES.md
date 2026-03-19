
**todo**

- Site Reports::Product: Web Compatibility - high value data we should optionally incorporate? Relevent bugs should get picked up in
    the crawl. Let's make sure that's happening.
- Themes - from here, how do we dive deeper?
    Facilitating the development of a software project around a theme.
- Neither tool likely understands the differences between processes and metrixc like crash rate.
- Github activity is a pretty big blind spot currently.

**both skills**
- Status table columns need standardization - | ASSIGNED S2 (padenot) | ? something like this.

**Good Suggestions from Claude**

- Add a socorro-cli --facet platform step when a crash signature is found to better characterize Windows vs Linux vs macOS distribution.
- The --date range comparison for crash trends didn't return results for older windows when the signature is newly emerging — could detect "new signature" vs "rising trend" as distinct signal categories.
- Consider automatically fetching the cc_count field via a targeted follow-up request when it is missing from the initial batch response.
    - it's always going to be missing if you don't have authentication. We'll need to prompt for this if we want to use it.
- The Graphics Triage Tracker meta (1632611) is a goldmine — consider fetching its 20 most-recently-changed deps as a standard step for the graphics scope.
- The cc_count field is systematically absent from Bugzilla REST API responses without authentication. The skill should document this more explicitly and suggest that comment_count is an acceptable substitute, or note that cc_count requires a logged-in API token to appear.