# Day 3 Performance Strategy

Day 3 works with Gold joins, aggregations, and possibly millions of records.

Recommended practices:

- select only required columns before joins
- aggregate one-to-many tables before joining
- broadcast only small dimensions when appropriate
- avoid unnecessary `.count()`
- inspect at least one `df.explain(True)`
- partition carefully
- avoid too many small files
- use Delta OPTIMIZE if available
- document limitations if OPTIMIZE/ZORDER is not available
