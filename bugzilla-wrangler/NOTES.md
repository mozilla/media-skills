
**todo**

- Site Reports::Product: Web Compatibility - high value data we should optionally incorporate? Relevent bugs should get picked up in
    the crawl. Let's make sure that's happening.
- Themes - from here, how do we dive deeper?
    Facilitating the development of a software project around a theme.
- Neither tool likely understands the differences between processes and metrics like crash rate.
- Github activity is a pretty big blind spot currently.

**both skills**
- Status table columns need standardization - | ASSIGNED S2 (padenot) | ? something like this.
- scope profiles and bugzilla - why can't we tie to scope to a bugzilla reference?

**Good Suggestions from Claude**

- Add a socorro-cli --facet platform step when a crash signature is found to better characterize Windows vs Linux vs macOS distribution.
- The --date range comparison for crash trends didn't return results for older windows when the signature is newly emerging — could detect "new signature" vs "rising trend" as distinct signal categories.
- Consider automatically fetching the cc_count field via a targeted follow-up request when it is missing from the initial batch response.
    - it's always going to be missing if you don't have authentication. We'll need to prompt for this if we want to use it.
- The Graphics Triage Tracker meta (1632611) is a goldmine — consider fetching its 20 most-recently-changed deps as a standard step for the graphics scope.
- The cc_count field is systematically absent from Bugzilla REST API responses without authentication. The skill should document this more explicitly and suggest that comment_count is an acceptable substitute, or note that cc_count requires a logged-in API token to appear.
- The --date window filter for socorro-cli did not return count-only output in the AGGREGATIONS block; the trend comparison relied on the FOUND count from the first lines. A dedicated count mode or structured JSON output from socorro-cli would make 30d/60d trend comparison more reliable.
- The Bugzilla REST API does not return cc_count when include_fields is specified alongside it. Augmenting seed enrichment with a secondary per-bug fetch for cc_count would allow more accurate signal scoring for the community-interest dimension.