## v1.3.0 (2024-05-26)

### Image versions
- datalens-control-api: 0.2066.0-rc.1 -> 0.2080.0 ([full changelog](https://github.com/datalens-tech/datalens-backend/compare/v0.2066.0-rc.1...v0.2080.0))
- datalens-data-api: 0.2066.0-rc.1 -> 0.2080.0 ([full changelog](https://github.com/datalens-tech/datalens-backend/compare/v0.2066.0-rc.1...v0.2080.0))
- datalens-ui: 0.1330.0 -> 0.1350.0 ([full changelog](https://github.com/datalens-tech/datalens-ui/compare/v0.1330.0...v0.1350.0))
- datalens-us: 0.170.0 -> 0.180.0 ([full changelog](https://github.com/datalens-tech/datalens-us/compare/v0.170.0...v0.180.0))

### Other
- Correct handle of no data case in markup wizard chart. [datalens-tech/datalens-ui#631](https://github.com/datalens-tech/datalens-ui/pull/631)
- Fix background color for null values in flat table. [datalens-tech/datalens-ui#634](https://github.com/datalens-tech/datalens-ui/pull/634)
- Add missing key. [datalens-tech/datalens-ui#635](https://github.com/datalens-tech/datalens-ui/pull/635)
- Fix title selection for segments. [datalens-tech/datalens-ui#637](https://github.com/datalens-tech/datalens-ui/pull/637)
- Fix rendering chart when line name matches with JavaScript Object properties. [datalens-tech/datalens-ui#639](https://github.com/datalens-tech/datalens-ui/pull/639)
- Update @gravity-ui/gateway to v2. [datalens-tech/datalens-ui#632](https://github.com/datalens-tech/datalens-ui/pull/632)
- Remove market_couriers connector data. [datalens-tech/datalens-ui#641](https://github.com/datalens-tech/datalens-ui/pull/641)
- Add keys consistency check for i18n keysets. [datalens-tech/datalens-ui#643](https://github.com/datalens-tech/datalens-ui/pull/643)
- Improve group controls improvements pt3. [datalens-tech/datalens-ui#616](https://github.com/datalens-tech/datalens-ui/pull/616)
- Update publish platform permission. [datalens-tech/datalens-ui#640](https://github.com/datalens-tech/datalens-ui/pull/640)
- Update mdb form i18n. [datalens-tech/datalens-ui#644](https://github.com/datalens-tech/datalens-ui/pull/644)
- New relations improvements. [datalens-tech/datalens-ui#647](https://github.com/datalens-tech/datalens-ui/pull/647)
- Update @gravity-ui/page-constructor to v4.52.0. [datalens-tech/datalens-ui#650](https://github.com/datalens-tech/datalens-ui/pull/650)
- Remove x-charts-id subrequest header. [datalens-tech/datalens-ui#646](https://github.com/datalens-tech/datalens-ui/pull/646)
- Add dashboard helpers for filtering tests. [datalens-tech/datalens-ui#605](https://github.com/datalens-tech/datalens-ui/pull/605)
- Use local chart editor templates. [datalens-tech/datalens-ui#606](https://github.com/datalens-tech/datalens-ui/pull/606)
- Fix aliases validation for the same dataset. [datalens-tech/datalens-ui#652](https://github.com/datalens-tech/datalens-ui/pull/652)
- Temporally disable tests. [datalens-tech/datalens-ui#657](https://github.com/datalens-tech/datalens-ui/pull/657)
- Add problematic alias to error output. [datalens-tech/datalens-ui#654](https://github.com/datalens-tech/datalens-ui/pull/654)
- Fix colors for the custom palette in the combined chart. [datalens-tech/datalens-ui#655](https://github.com/datalens-tech/datalens-ui/pull/655)
- Data fetcher proxied headers refactoring. [datalens-tech/datalens-ui#651](https://github.com/datalens-tech/datalens-ui/pull/651)
- ci: add DOCKER_HOST to env Taskfile. [datalens-tech/datalens-backend#374](https://github.com/datalens-tech/datalens-backend/pull/374)
- BI-5267 Add execution timeout to PG connector; use readonly transactions in PG. [datalens-tech/datalens-backend#375](https://github.com/datalens-tech/datalens-backend/pull/375)
- Fix source execution timeout for ClickHouse by lowering it. [datalens-tech/datalens-backend#376](https://github.com/datalens-tech/datalens-backend/pull/376)
- Preparing for migrations. [datalens-tech/datalens-us#87](https://github.com/datalens-tech/datalens-us/pull/87)
- Fix billingInstanceServiceIdPrefix missed error code. [datalens-tech/datalens-us#90](https://github.com/datalens-tech/datalens-us/pull/90)
- Add execution timeout to MSSQL connector. [datalens-tech/datalens-backend#377](https://github.com/datalens-tech/datalens-backend/pull/377)
- Change YADOCS_INVALID_PUBLIC_LINK_PREFIX from 500 to 400. [datalens-tech/datalens-backend#379](https://github.com/datalens-tech/datalens-backend/pull/379)
- Add two billing migrations. [datalens-tech/datalens-us#89](https://github.com/datalens-tech/datalens-us/pull/89)
- Run US migrations before tests. [datalens-tech/datalens-backend#371](https://github.com/datalens-tech/datalens-backend/pull/371)
- Remove uwsgi from file uploader. [datalens-tech/datalens-backend#380](https://github.com/datalens-tech/datalens-backend/pull/380)
- Up jest. [datalens-tech/datalens-us#91](https://github.com/datalens-tech/datalens-us/pull/91)
- Run mypy in parallel. [datalens-tech/datalens-backend#373](https://github.com/datalens-tech/datalens-backend/pull/373)
- execute-mypy-multi: make parameters named, run mypy in parallel. [datalens-tech/datalens-backend#381](https://github.com/datalens-tech/datalens-backend/pull/381)
- Add returning full collection models in getCollectionBreadcrumbs. [datalens-tech/datalens-us#93](https://github.com/datalens-tech/datalens-us/pull/93)
- Add new billing fields. [datalens-tech/datalens-us#92](https://github.com/datalens-tech/datalens-us/pull/92)
- fix some mypy in dl_formula.shortcuts. [datalens-tech/datalens-backend#383](https://github.com/datalens-tech/datalens-backend/pull/383)
- Improve workbook isolation. [datalens-tech/datalens-us#96](https://github.com/datalens-tech/datalens-us/pull/96)
- Fix US storage schema of yadocs connection source. [datalens-tech/datalens-backend#386](https://github.com/datalens-tech/datalens-backend/pull/386)
- remove an erroneous type check on making a join expression. [datalens-tech/datalens-backend#385](https://github.com/datalens-tech/datalens-backend/pull/385)
- Add some profiling to mutation caches; propagate allow_slave up to dataset preparer. [datalens-tech/datalens-backend#378](https://github.com/datalens-tech/datalens-backend/pull/378)
- Add npm migration scripts. [datalens-tech/datalens-us#97](https://github.com/datalens-tech/datalens-us/pull/97)
- Switch to port 8083. [datalens-tech/datalens-us#98](https://github.com/datalens-tech/datalens-us/pull/98)
- Update US port. [datalens-tech/datalens-backend#392](https://github.com/datalens-tech/datalens-backend/pull/392)
- Upgrade gitpython to >=3.1.41. [datalens-tech/datalens-backend#393](https://github.com/datalens-tech/datalens-backend/pull/393)
- feat: add ActionNonStreamExecuteQuery to RQE. [datalens-tech/datalens-backend#388](https://github.com/datalens-tech/datalens-backend/pull/388)
- Add createWorkbook to api. [datalens-tech/datalens-us#99](https://github.com/datalens-tech/datalens-us/pull/99)
- Allow NULL as a default for LAG in CH. [datalens-tech/datalens-backend#395](https://github.com/datalens-tech/datalens-backend/pull/395)
- Add avatar relation "required" field to the storage schema. [datalens-tech/datalens-backend#399](https://github.com/datalens-tech/datalens-backend/pull/399)
- Fix 'argument not bound to an attrs class' mypy errors. [datalens-tech/datalens-backend#394](https://github.com/datalens-tech/datalens-backend/pull/394)
- fix: rqe_execute_request_mode env_var_converter. [datalens-tech/datalens-backend#400](https://github.com/datalens-tech/datalens-backend/pull/400)
- Fix UpdateConnectionDataRequestSchema. [datalens-tech/datalens-backend#401](https://github.com/datalens-tech/datalens-backend/pull/401)
- Print affected packages in router. [datalens-tech/datalens-backend#403](https://github.com/datalens-tech/datalens-backend/pull/403)
- Add COLOR, SIZE, BR to docs & suggest. [datalens-tech/datalens-backend#382](https://github.com/datalens-tech/datalens-backend/pull/382)
- Revert CH max_execution_time parameter. [datalens-tech/datalens-backend#404](https://github.com/datalens-tech/datalens-backend/pull/404)
- Fix some type annotations, cleanup. [datalens-tech/datalens-backend#397](https://github.com/datalens-tech/datalens-backend/pull/397)
- feat: add dl_rate_limiter. [datalens-tech/datalens-backend#402](https://github.com/datalens-tech/datalens-backend/pull/402)
- feat: remove bitrix join experimental flag. [datalens-tech/datalens-backend#406](https://github.com/datalens-tech/datalens-backend/pull/406)
- DOCSUP-66197: Fixes in function ref texts. [datalens-tech/datalens-backend#391](https://github.com/datalens-tech/datalens-backend/pull/391)
- Added overridable method get_session_cookies to AiohttpDBAdapter. [datalens-tech/datalens-backend#407](https://github.com/datalens-tech/datalens-backend/pull/407)
- Enable mysql OS. [datalens-tech/datalens-backend#409](https://github.com/datalens-tech/datalens-backend/pull/409)
- add custom error code for workbook isolation error. [datalens-tech/datalens-backend#358](https://github.com/datalens-tech/datalens-backend/pull/358)
- Turn on greenplum os. [datalens-tech/datalens-backend#410](https://github.com/datalens-tech/datalens-backend/pull/410)
- Image markup. [datalens-tech/datalens-backend#408](https://github.com/datalens-tech/datalens-backend/pull/408)
- feat: add app rate_limiter settings. [datalens-tech/datalens-backend#411](https://github.com/datalens-tech/datalens-backend/pull/411)
- tests: mark rate_limiter middleware tests flaky. [datalens-tech/datalens-backend#412](https://github.com/datalens-tech/datalens-backend/pull/412)
- replace some TypeVars with typing_extensions.Self. [datalens-tech/datalens-backend#396](https://github.com/datalens-tech/datalens-backend/pull/396)
- Refine required relations & JOINs optimization. [datalens-tech/datalens-backend#414](https://github.com/datalens-tech/datalens-backend/pull/414)
- fix: yet another fix for rate limiter settings. [datalens-tech/datalens-backend#415](https://github.com/datalens-tech/datalens-backend/pull/415)
- fix: yet another fix for rate limiter settings. [datalens-tech/datalens-backend#416](https://github.com/datalens-tech/datalens-backend/pull/416)
- fix: rate_limiter config. [datalens-tech/datalens-backend#417](https://github.com/datalens-tech/datalens-backend/pull/417)
- Move YQL datetime functions to the YDB connector package. [datalens-tech/datalens-backend#413](https://github.com/datalens-tech/datalens-backend/pull/413)
- DLHELP-9856: add more logs to file connectors. [datalens-tech/datalens-backend#418](https://github.com/datalens-tech/datalens-backend/pull/418)
- feat: temporarily disable rate_limiter settings. [datalens-tech/datalens-backend#419](https://github.com/datalens-tech/datalens-backend/pull/419)
- Moved get_data_source_template_templates method implementation from ConnectionCHYTToken to BaseConnectionCHYT. [datalens-tech/datalens-backend#421](https://github.com/datalens-tech/datalens-backend/pull/421)
- Markup image fix. [datalens-tech/datalens-backend#420](https://github.com/datalens-tech/datalens-backend/pull/420)


## v1.2.0 (2024-05-26)

### Image versions
- datalens-control-api: 0.2063.0-rc.1 -> 0.2066.0-rc.1 ([full changelog](https://github.com/datalens-tech/datalens-backend/compare/v0.2063.0-rc.1...v0.2066.0-rc.1))
- datalens-data-api: 0.2063.0-rc.1 -> 0.2066.0-rc.1 ([full changelog](https://github.com/datalens-tech/datalens-backend/compare/v0.2063.0-rc.1...v0.2066.0-rc.1))
- datalens-ui: 0.1316.0 -> 0.1330.0 ([full changelog](https://github.com/datalens-tech/datalens-ui/compare/v0.1316.0...v0.1330.0))
- datalens-us: 0.159.0 -> 0.170.0 ([full changelog](https://github.com/datalens-tech/datalens-us/compare/v0.159.0...v0.170.0))

### Breaking changes
- Fix bigquery dependencies (add a required pyarrow extra). [datalens-tech/datalens-backend#365](https://github.com/datalens-tech/datalens-backend/pull/365)
- Implemented typed query processor factories in SR. [datalens-tech/datalens-backend#367](https://github.com/datalens-tech/datalens-backend/pull/367)

### New features
- **Connectors**, **Datasets**. Removing ExecutorBasedMixin. Part 2. [datalens-tech/datalens-backend#345](https://github.com/datalens-tech/datalens-backend/pull/345)

### CI
- Fixed circular import dependencies in api connector. [datalens-tech/datalens-backend#344](https://github.com/datalens-tech/datalens-backend/pull/344)

### Other
- Improve GroupControls behavior. [datalens-tech/datalens-ui#596](https://github.com/datalens-tech/datalens-ui/pull/596)
- Fix the test falling at midnight. [datalens-tech/datalens-ui#618](https://github.com/datalens-tech/datalens-ui/pull/618)
- Fix i18n flow. [datalens-tech/datalens-ui#617](https://github.com/datalens-tech/datalens-ui/pull/617)
- Fix export forbidden fail in chartEditor. [datalens-tech/datalens-ui#620](https://github.com/datalens-tech/datalens-ui/pull/620)
- Fix buttons position on mobile fullscreen. [datalens-tech/datalens-ui#603](https://github.com/datalens-tech/datalens-ui/pull/603)
- Fix dashboard publish link xss. [datalens-tech/datalens-ui#612](https://github.com/datalens-tech/datalens-ui/pull/612)
- Fix resolveUsersByIds mock. [datalens-tech/datalens-ui#621](https://github.com/datalens-tech/datalens-ui/pull/621)
- Fix displaying alias modal on select ignore link. [datalens-tech/datalens-ui#623](https://github.com/datalens-tech/datalens-ui/pull/623)
- Workbook page redesign. [datalens-tech/datalens-ui#562](https://github.com/datalens-tech/datalens-ui/pull/562)
- Add changelog label to release comment. [datalens-tech/datalens-ui#626](https://github.com/datalens-tech/datalens-ui/pull/626)
- Disable test and lints for translation branches. [datalens-tech/datalens-ui#625](https://github.com/datalens-tech/datalens-ui/pull/625)
- Add new label to release. [datalens-tech/datalens-ui#627](https://github.com/datalens-tech/datalens-ui/pull/627)
- Change onRender -> onLoad for MarkupWidget. [datalens-tech/datalens-ui#629](https://github.com/datalens-tech/datalens-ui/pull/629)
- Update docker-compose.e2e.yml. [datalens-tech/datalens-ui#628](https://github.com/datalens-tech/datalens-ui/pull/628)
- Update @gravity-ui/gateway. [datalens-tech/datalens-us#77](https://github.com/datalens-tech/datalens-us/pull/77)
- Add migration for change index tenants_billing_instance_service_id_id on UNIQUE. [datalens-tech/datalens-us#76](https://github.com/datalens-tech/datalens-us/pull/76)
- Some naming fixes. [datalens-tech/datalens-us#78](https://github.com/datalens-tech/datalens-us/pull/78)
- Remove favorites migration. [datalens-tech/datalens-us#80](https://github.com/datalens-tech/datalens-us/pull/80)
- Add foreign key (entry_id, tenant_id) for favorites (2). [datalens-tech/datalens-us#81](https://github.com/datalens-tech/datalens-us/pull/81)
- Add yadocs to file connections. [datalens-tech/datalens-us#82](https://github.com/datalens-tech/datalens-us/pull/82)
- Added branding column to tenants table. [datalens-tech/datalens-us#85](https://github.com/datalens-tech/datalens-us/pull/85)
- Specify correct data source spec in GP dsrc migrator (inherit GP dsrc migrator from PG). [datalens-tech/datalens-backend#336](https://github.com/datalens-tech/datalens-backend/pull/336)
- Move some model-related modules to dl_model_tools. [datalens-tech/datalens-backend#363](https://github.com/datalens-tech/datalens-backend/pull/363)
- Moved a couple of modules out of dl_core. [datalens-tech/datalens-backend#362](https://github.com/datalens-tech/datalens-backend/pull/362)
- Fixes in function ref texts. [datalens-tech/datalens-backend#364](https://github.com/datalens-tech/datalens-backend/pull/364)
- Add existing operation codes for us client. [datalens-tech/datalens-backend#369](https://github.com/datalens-tech/datalens-backend/pull/369)
- Get rid of templateTenantId. [datalens-tech/datalens-us#83](https://github.com/datalens-tech/datalens-us/pull/83)
- Add new error for existing serviceInstanceIdPrefix in cofig. [datalens-tech/datalens-us#88](https://github.com/datalens-tech/datalens-us/pull/88)
- Added branding handlers. [datalens-tech/datalens-us#86](https://github.com/datalens-tech/datalens-us/pull/86)
- **Connectors**. Implemented CachedTypedQueryProcessor. [datalens-tech/datalens-backend#372](https://github.com/datalens-tech/datalens-backend/pull/372)


## v1.1.0 (2024-03-17)

### Image versions
- datalens-control-api: 0.2061.0-rc.1 -> 0.2063.0-rc.1 ([full changelog](https://github.com/datalens-tech/datalens-backend/compare/v0.2061.0-rc.1...v0.2063.0-rc.1))
- datalens-data-api: 0.2061.0-rc.1 -> 0.2063.0-rc.1 ([full changelog](https://github.com/datalens-tech/datalens-backend/compare/v0.2061.0-rc.1...v0.2063.0-rc.1))
- datalens-ui: 0.1316.0
- datalens-us: 0.159.0
- test update

### Other
- ci: release prerelease in parallel with build images step. [datalens-tech/datalens-backend#361](https://github.com/datalens-tech/datalens-backend/pull/361)
- Remove useless null check. [datalens-tech/datalens-backend#360](https://github.com/datalens-tech/datalens-backend/pull/360)


## v1.0.0 (2024-05-26)

### Changes
- Introduce the new versioning system


## 2024-02-22

### Updated images
- datalens-control-api: 0.2046.0 -> 0.2048.2
- datalens-data-api: 0.2046.0 -> 0.2048.2

### Changes

- Minor improvements

## 2024-02-16

### Updated images
- datalens-us: 0.157.0 -> 0.159.0
- datalens-ui: 0.1296.0 -> 0.1316.0

### Changed

- Refactored logic of displaying new relations ([ui:#602](https://github.com/datalens-tech/datalens-ui/pull/602))
- Fix preload dark theme ([ui:#610](https://github.com/datalens-tech/datalens-ui/pull/610))
- Fix chart coloring with null value ([ui:#593](https://github.com/datalens-tech/datalens-ui/pull/593))
- Fix axis labels formatting for bar charts  ([ui:#592](https://github.com/datalens-tech/datalens-ui/pull/592))

## 2024-02-09

### Updated images
- datalens-us: 0.149.0 -> 0.157.0
- datalens-ui: 0.1268.0 -> 0.1296.0

### Changed
- Support inner label in datepicker control ([ui:#566](https://github.com/datalens-tech/datalens-ui/pull/566))
- Add required selector option ([ui:#563](https://github.com/datalens-tech/datalens-ui/pull/563))
- Add dash ActionPanel animation ([ui:#560](https://github.com/datalens-tech/datalens-ui/pull/560))
- Fix remove alias area, fix alias controls icons displaying ([ui:#585](https://github.com/datalens-tech/datalens-ui/pull/585))
- Fix flat table gradient coloring ([ui:#559](https://github.com/datalens-tech/datalens-ui/pull/559))

## 2024-02-02

### Updated images
- datalens-us: 0.143.0 -> 0.149.0
- datalens-ui: 0.1245.0 -> 0.1268.0

### Changed
- Changed hide retry on some errors ([ui:#532](https://github.com/datalens-tech/datalens-ui/pull/532))
- Fix charts with params and datasets relations ([ui:#521](https://github.com/datalens-tech/datalens-ui/pull/521))
- Fix save button behaviour for QL charts ([ui:#548](https://github.com/datalens-tech/datalens-ui/pull/548))
- Fix bundlesize ([ui:#551](https://github.com/datalens-tech/datalens-ui/pull/551))

## 2024-01-26

### Updated images
- datalens-us: 0.133.0 -> 0.143.0
- datalens-ui: 0.1137.0 -> 0.1245.0

### Changed
- Add line support for d3 visualizations ([ui:#334](https://github.com/datalens-tech/datalens-ui/pull/334))
- Add shapes support for d3 visualizations ([ui:#516](https://github.com/datalens-tech/datalens-ui/pull/516))
- Add postgres env vars for US ([us:#54](https://github.com/datalens-tech/datalens-us/pull/54))
- Disable old relations ([ui:#518](https://github.com/datalens-tech/datalens-ui/pull/518))
- Fix removing comments in QL charts ([ui:#523](https://github.com/datalens-tech/datalens-ui/pull/523))
- Fix chart autoHeight calculation ([ui:#482](https://github.com/datalens-tech/datalens-ui/pull/482))

## 2024-01-24

### Updated images
- datalens-control-api: 0.2042.0 -> 0.2046.0
- datalens-data-api: 0.2042.0 -> 0.2046.0

### Changed

- Switched datalens-control-api and datalens-data-api containers to rootless mode
- Updated datalens-control-api & datalens-data-api base image from Ubuntu 20.04 to 22.04
- Fixed dataset loading when the connection is deleted
- Constant expressions are now removed from GROUP BY during query compilation

## 2024-01-20
- Add `UI_PORT` env param

## 2024-01-15
- Add `docker-compose-dev.yml`

## 2023-12-27

### Updated images
- datalens-control-api: 0.2040.0 -> 0.2042.0
- datalens-data-api: 0.2040.0 -> 0.2042.0

### Changed

- Enabled YDB connector

## 2023-12-26

### Updated images
- datalens-us: 0.132.0 -> 0.133.0
- datalens-ui: 0.1113.0 -> 0.1137.0

### Changed
- Added export to Excel feature
- Fix opening dash widget dialog with active widget tab
- Small interface improvements and bugfixies
- Fixed Apple M-series chips compatibility

## 2023-12-21

### Updated images
- datalens-control-api: 0.2038.1 -> 0.2040.0
- datalens-data-api: 0.2038.1 -> 0.2040.0
- datalens-us: 0.116.0 -> 0.132.0
- datalens-ui: 0.955.0 -> 0.1113.0

### Changed

- Updated system dependencies to fix vulnerabilities
- datalens-ui and datalens-us containers switched to rootless mode
- Fix table markup sorting
- Fix colors and shapes by field with prefix/postfix in title
- Fix ColorMode behaviour for bar charts
- New datepicker with relative dates for parameters in QL
- Add beta relations on dashboards
- Improve create dash entry without filling name first
- Collections & workbooks sorting fix
- Improve mobile dashboard page, added TOC & improve header mobile view


## 2023-11-24

### Updated images
- datalens-control-api: 0.2038.0 -> 0.2038.1
- datalens-data-api: 0.2038.0 -> 0.2038.1
- datalens-us: 0.110.0 -> 0.116.0

### Changed

- Add demo wokbook with local PostgreSQL database

## 2023-11-15

### Updated images
- datalens-control-api: 0.2037.0 -> 0.2038.0
- datalens-data-api: 0.2037.0 -> 0.2038.0
- datalens-us: 0.96.0 -> 0.110.0
- datalens-ui: 0.795.0 -> 0.966.0

### Changed
- UI improvements for dashboard editings
- Fixed gradient color settings on pie and pie charts
- UI improvements for workbooks (buttons grouping)
- QL charts: implemented a '+' button to add fields
