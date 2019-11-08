---
ID: 107
post_title: >
  1.6 Open science practice, reproducible
  workflow, and data management
author: jonathans
post_excerpt: ""
layout: post
permalink: >
  http://climexhandbook.w.uib.no/2019/11/07/open-science-practice-reproducible-workflow-and-data-management/
published: true
post_date: 2019-11-07 01:00:56
---
Many ecological questions nowadays are related to complex drivers and mechanisms on large spatial and temporal scales which increasingly demands collaborations (i.e. research networks), handling of large datasets, and data sharing. For this, the study design, data analysis, and results need to be correctly and comprehensively reported, which are surprisingly often not the case (Hillebrand &amp; Gurevitch, 2013; Haddaway &amp; Verhoeven, 2015), frustrating researchers aiming to synthesise and upscale research developments (Halbritter et al., 2018; Morueta-Holme et al., 2018). Open science practice, reproducible workflow, and data management have recently received much attention in ecology and in science and when successfully applied these practises ensure high-quality data, which is available to others and in the future (Lind 2013). Funding bodies and publishers have recognised this and now often ask for a data management plan and open science practice (British Ecological Society, 2018). “Prereproducible” practise – a holistic approach of providing sufficient information about data and workflow – is becoming more common (Stark, 2018).

Data management is the planning of the “data cycle” in a research project, including how to create, process, document, share, store, and re-use the data (British Ecological Society, 2018). It can be applied to small and large projects and should be planned well ahead of the start of a project.

Alongside the planning of the study design and research questions, the workflow from collecting raw data, to the final results, should be planned, i.e. data curation, transformations, quality check, visual examination and analysis, data storage, and data availability beyond the project (create, process and store data). The raw data should always be retained and the workflow should follow a well-documented and script-based approach. This allows the script to be revised and rerun at any time and thus ensures transparency, reproducibility, and a robust workflow (British Ecological Society, 2017). Version control such as Git combined with a host (e.g. GitHub, Bitbucket) ensures transparency and reproducibility of the workflow. The data should always be stored in non-proprietary software formats to ensure long-term availability beyond the project. A common practice in medical and social sciences to enhance good research practice, though rarely applied in ecology, is to preregister the planned data analysis (Nosek et al., 2015). This ensures a thorough thinking about what data and analysis are needed and reduces problematic research practice (e.g. clarifies projects aims vs. hypothesis-testing or hypothesis-generating research, reduces risk of cherry picking; Fraser et al., 2018).

Thorough data documentation and metadata ensures that the data are available in the long term. Data documentation should be started early, done consistently, and updated regularly to ensure an overview of the methodology, data, data manipulation, and analysis. Complete data documentation and metadata is important for inter-study comparisons (see above) and enables data sharing and re-use.

Here we provide a list for how to correctly report study design, data analysis, and results from climate-change studies to make research reproducible and for synthesis (Table 1.6.1). This table was compiled from Hillbrand &amp; Gurevitch (2013), Haddaway &amp; Verhoeven (2015), and Gerstner et al. (2017).

<strong>Table 1.6.1</strong> Issues and guidance for how to correctly report study design, data analysis, and results from climate-change studies. Adapted from Hillbrand &amp; Gurevitch (2013), Haddaway &amp; Verhoeven (2015), and Gerstner et al. (2017).
<table style="width: 100%" width="603">
<tbody>
<tr>
<td style="vertical-align: top;width: 19.0037%" width="120"><strong> </strong></td>
<td style="text-align: left;vertical-align: top;width: 26.6605%" width="167"><strong>Issue</strong></td>
<td style="text-align: left;vertical-align: top;width: 54.2436%" width="316"><strong>Guidance</strong></td>
</tr>
<tr>
<td style="text-align: left;vertical-align: top;width: 19.0037%" width="120"><strong>General</strong></td>
<td style="text-align: left;vertical-align: top;width: 26.6605%" width="167"><em>Methodology </em>

<em> </em><em> </em>

<em>Necessary meta-data provided</em>

<em> </em>

<em> </em>

<em> </em><em> </em>

<em>Data and study should be easy to find, and be accessible.</em></td>
<td style="text-align: left;vertical-align: top;width: 54.2436%" width="316">Each study and dataset should be described in detail in a readme file, including a data dictionary and annotated dataset (Table 1.6.2; British Ecological Society, 2018).

Correctly report site characteristics: i.e. geographic location, elevation, vegetation type, soil physical and chemical properties, meteorological data (see protocols 1.2 - 1.5), and author information.

Results (including master theses, internal reports, etc.) should be publicly available.

Data should be publicly available in a data repository. Funding bodies and journals are increasingly requiring this.

Publications should have useful keywords and titles to enable them to be easily found.</td>
</tr>
<tr>
<td style="text-align: left;vertical-align: top;width: 19.0037%" width="120"><strong>Study design</strong></td>
<td style="text-align: left;vertical-align: top;width: 26.6605%" width="167"><em>Study design is reported in sufficient detail</em></td>
<td style="text-align: left;vertical-align: top;width: 54.2436%" width="316">The description of the study design should be thorough; parts of it can be reported in the appendix if there is limited space. Correctly report:
<p style="padding-left: 40px">●   start, end date, and duration of the study</p>
<p style="padding-left: 40px">●   treatment factors, levels, and interactions, design structure, e.g. factorial, nested, hierarchical</p>
<p style="padding-left: 40px">●   level of replication: number of sites, blocks, plots, and sub-plots; including selection and randomisation process at each level</p>
<p style="padding-left: 40px">●   spatial scale: size of the study unit, distance between sites, populations</p>
<p style="padding-left: 40px">●   type of data sampled (predictors and covariates), and sampling precision for each (including any within‐replicate sampling or pseudoreplication)</p>
<p style="padding-left: 40px">●   sampling schedule: timing, frequency, including study design aspects such as treatment-control, before-after-control-impact, etc. (also see Table 1.1)</p>
<p style="padding-left: 40px">●   description of the manipulated organism, population, or community should follow accepted taxonomic literature, e.g. The Plant List (TPL; http://www.theplantlist.org/) and the Taxonomic Name Resolution Service (TNRS; Boyle et al., 2013) and national or international classification schemes.</p>
</td>
</tr>
<tr>
<td style="text-align: left;vertical-align: top;width: 19.0037%" width="120"><strong>Response variables, predictors, and covariates</strong></td>
<td style="text-align: left;vertical-align: top;width: 26.6605%" width="167"><em>Measurements should be relevant, reproducible, and convertible</em></td>
<td style="text-align: left;vertical-align: top;width: 54.2436%" width="316">Follow established protocols, and guidance on which and how to measure predictors, response variables, and covariates.

Report which protocols are used, and describe any adjustments that are made.

Describe all variables fully and report in readme files, data dictionaries, and datasets.

Measure useful covariates for synthesis and upscaling (see Table 2 in the main paper).</td>
</tr>
<tr>
<td style="text-align: left;vertical-align: top;width: 19.0037%" width="120"><strong>Data handling and analysis</strong></td>
<td style="text-align: left;vertical-align: top;width: 26.6605%" width="167"><em>Data manipulation is described in sufficient detail</em>

<em>Comprehensive description of data analysis</em><em> </em>

&nbsp;

<em> </em><em> </em>

<em>Reproducible workflow</em></td>
<td style="text-align: left;vertical-align: top;width: 54.2436%" width="316">Each step of data manipulation should be described and explained and be repeatable and reproducible (British Ecological Society, 2017).

Type of statistical tests used, response variables, covariates (explanatory factors) tested, posthoc or planned comparisons carried out, definition of statistical metrics if different from commonly accepted terms should be described.

Statistical software, packages, and versions used need to be reported.

The workflow from data manipulation, coding, analysing, and results output should be repeatable and reproducible (Lind 2013, British Ecological Society, 2017).</td>
</tr>
<tr>
<td style="text-align: left;vertical-align: top;width: 19.0037%" width="120"><strong>Results</strong></td>
<td style="text-align: left;vertical-align: top;width: 26.6605%" width="167"><em>Units need to be reported</em>

<em>Raw data should be provided</em>

&nbsp;

<em>Negative results should be reported</em></td>
<td style="text-align: left;vertical-align: top;width: 54.2436%" width="316">Units for each variable should be reported.

Raw data or summary statistics with mean (or median), variation around the mean and sample size should be reported.

Report negative results.</td>
</tr>
</tbody>
</table>
&nbsp;

<span style="font-size: 10pt"><strong>Table 1.6.2</strong> Content for a readme file for a research project and a data dictionary.</span>
<table style="border-collapse: collapse;width: 82.6568%">
<tbody>
<tr>
<td style="width: 100%;text-align: left"><strong>a) Readme file</strong>
<ol>
 	<li style="list-style-type: none">
<ol>
 	<li>Project information
<ol style="list-style-type: lower-alpha">
 	<li>Project summary</li>
 	<li>Funding information</li>
 	<li>Primary contact information</li>
 	<li>Project partners, students, collaborators</li>
 	<li>Research sites and basic site information</li>
 	<li>Information on data repositories</li>
 	<li>Naming conventions for data files, datasets, co-variables (taxa, studies/experiments, treatments, sites), response variables</li>
 	<li>Data access, authorship rights, data policy and acknowledgements</li>
</ol>
</li>
 	<li>Studies and/or experiments</li>
 	<li>Publications
<ol style="list-style-type: lower-alpha">
 	<li>Publications</li>
 	<li>Master/doctoral theses, reports etc.</li>
</ol>
</li>
 	<li>References</li>
</ol>
</li>
</ol>
&nbsp;</td>
</tr>
<tr>
<td style="width: 100%;text-align: left"><strong>b) Data dictionary</strong>
<ol>
 	<li style="list-style-type: none">
<ol>
 	<li>Content of the dataset</li>
 	<li>Data collection methods</li>
 	<li>Dataset authors and collaborators</li>
 	<li>Location of data collection</li>
 	<li>Time of data collection</li>
 	<li>Study design</li>
 	<li>Data development and curation</li>
 	<li>Other relevant datasets within the project (e.g. predictors)</li>
 	<li>Data usage – publications</li>
 	<li>Data dictionary (variable name, type, range, factor level, measurement type and unit/format)</li>
</ol>
</li>
</ol>
</td>
</tr>
</tbody>
</table>
&nbsp;

<strong><em>Where to start?</em></strong>

Gerstner et al. (2017) give guidance on how to make the reach of your research broader and longer lasting; Haddaway &amp; Verhoeven (2015) explain how to correctly describe methodology in ecology to make the research repeatable; Hillebrand and Gurevitch (2013) provide a checklist for reporting study details in manuscripts. The British Ecological Society (2017) have produced a useful guide for Reproducible Code in Ecology and Evolution. Lind (2013) presents lessons learned about data management in NutNet.

&nbsp;
<h4><a name="_Toc23712722"></a><strong>1.6.1 References</strong></h4>
Boyle, B., Hopkins, N., Lu, Z., Raygoza Garay, J. A., Mozzherin, D., Rees, T., … Enquist, B. J. (2013). The taxonomic name resolution service: an online tool for automated standardization of plant names.<em> BMC Bioinformatics</em>, 14, 16.

British Ecological Society. (2017). <em>A Guide to Reproducible Code in Ecology and Evolution</em>. (K. Harrison, Ed.). British Ecological Society. Retrieved from www.britishecologicalsociety.org/publications/guides-to/

British Ecological Society. (2018).<em> A Guide to Data Management in Ecology and Evolution</em>. (K. Harrison, Ed.). British Ecological Society. Retrieved from www.britishecologicalsociety.org/publications/guides-to/

Fraser, L. H., Henry, H. A. L., Carlyle, C. N., White, S. R., Beierkuhnlein, C., Cahill, J. F., … Turkington, R. (2013). Coordinated distributed experiments: an emerging tool for testing global hypotheses in ecology and environmental science. <em>Frontiers in Ecology and the Environment</em>, 11(3), 147–155.

Gerstner, K., Moreno-Mateos, D., Gurevitch, J., Beckmann, M., Kambach, S., Jones, H. P., &amp; Seppelt, R. (2017). Will your paper be used in a meta-analysis? Make the reach of your research broader and longer lasting. <em>Methods in Ecology and Evolution</em>, 8(6), 777–784.

Haddaway, N. R., &amp; Verhoeven, J. T. A. (2015). Poor methodological detail precludes experimental repeatability and hampers synthesis in ecology. <em>Ecology and Evolution</em>, 5(19), 4451–4454.

Halbritter, A. H., Fior, S., Keller, I., Billeter, R., Edwards, P. J., Holderegger, R., … Alexander, J. M. (2018). Trait differentiation and adaptation of plants along elevation gradients. <em>Journal of Evolutionary Biology</em>, 31, 784–800.

Hillebrand, H., &amp; Gurevitch, J. (2013). Reporting standards in experimental studies.<em> Ecology Letters</em>, 16(12), 1419–1420.

Lind, E. M. (2016). Unified data management for distributed experiments: A model for collaborative grassroots scientific networks. <em>Ecological informatics</em>, 36, 231–236.

Morueta-Holme, N., Oldfather, M. F., Olliff-Yang, R. L., Weitz, A. P., Levine, C. R., Kling, M. M., … Ackerly, D. D. (2018). Best practices for reporting climate data in ecology. <em>Nature Climate Change</em>, 8(2), 92–94.

Nosek, B. A., Alter, G., Banks, G. C., Borsboom, D., Bowman, S. D., Breckler, S. J., … Yarkoni, T. (2015). Promoting an open research culture. <em>Science</em>, 348(6242), 1422–1425.

Stark, P. B. (2018). Before reproducibility must come preproducibility. <em>Nature</em>, 557(7707), 613.