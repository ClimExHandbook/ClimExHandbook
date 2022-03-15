

## Open science practice, reproducible workflow, and data management

Many ecological questions nowadays are related to complex drivers and mechanisms on large spatial and temporal scales which increasingly demands collaborations (i.e. research networks), handling of large datasets, and data sharing. For this, the study design, data analysis, and results need to be correctly and comprehensively reported, which are surprisingly often not the case (Hillebrand & Gurevitch, 2013; Haddaway & Verhoeven, 2015), frustrating researchers aiming to synthesise and upscale research developments (Halbritter et al., 2018; Morueta-Holme et al., 2018). Open science practice, reproducible workflow, and data management have recently received much attention in ecology and in science and when successfully applied these practises ensure high-quality data, which is available to others and in the future (Lind 2013). Funding bodies and publishers have recognised this and now often ask for a data management plan and open science practice (British Ecological Society, 2018). “Prereproducible” practise – a holistic approach of providing sufficient information about data and workflow – is becoming more common (Stark, 2018).

Data management is the planning of the “data cycle” in a research project, including how to create, process, document, share, store, and re-use the data (British Ecological Society, 2018). It can be applied to small and large projects and should be planned well ahead of the start of a project. 

Alongside the planning of the study design and research questions, the workflow from collecting raw data, to the final results, should be planned, i.e. data curation, transformations, quality check, visual examination and analysis, data storage, and data availability beyond the project (create, process and store data). The raw data should always be retained and the workflow should follow a well-documented and script-based approach. This allows the script to be revised and rerun at any time and thus ensures transparency, reproducibility, and a robust workflow (British Ecological Society, 2017). Version control such as Git combined with a host (e.g. GitHub, Bitbucket) ensures transparency and reproducibility of the workflow. The data should always be stored in non-proprietary software formats to ensure long-term availability beyond the project. A common practice in medical and social sciences to enhance good research practice, though rarely applied in ecology, is to preregister the planned data analysis (Nosek et al., 2015). This ensures a thorough thinking about what data and analysis are needed and reduces problematic research practice (e.g. clarifies projects aims vs. hypothesis-testing or hypothesis-generating research, reduces risk of cherry picking; Fraser et al., 2018).

Thorough data documentation and metadata ensures that the data are available in the long term. Data documentation should be started early, done consistently, and updated regularly to ensure an overview of the methodology, data, data manipulation, and analysis. Complete data documentation and metadata is important for inter-study comparisons (see above) and enables data sharing and re-use.

Here we provide a list for how to correctly report study design, data analysis, and results from climate-change studies to make research reproducible and for synthesis (Table \@ref(tab:reproting)). This table was compiled from Hillbrand & Gurevitch (2013), Haddaway & Verhoeven (2015), and Gerstner et al. (2017).



<table>
<caption>(\#tab:reproting)Issues and guidance for how to correctly report study design, data analysis, and results from climate-change studies. Adapted from Hillbrand &amp; Gurevitch (2013), Haddaway &amp; Verhoeven (2015), and Gerstner et al. (2017).</caption>
 <thead>
  <tr>
   <th style="text-align:left;">  </th>
   <th style="text-align:left;"> Guidance </th>
   <th style="text-align:left;"> General </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;font-weight: bold;width: 10em; "> General </td>
   <td style="text-align:left;font-style: italic;width: 10em; "> _Methodology_ </td>
   <td style="text-align:left;"> Each study and dataset should be described in detail in a readme file, including a data dictionary and annotated dataset (Table 1.6.2; British Ecological Society, 2018). </td>
  </tr>
  <tr>
   <td style="text-align:left;font-weight: bold;width: 10em; "> General </td>
   <td style="text-align:left;font-style: italic;width: 10em; "> _Necessary meta-data provided_ </td>
   <td style="text-align:left;"> Correctly report site characteristics: i.e. geographic location, elevation, vegetation type, soil physical and chemical properties, meteorological data (see protocols 1.2 - 1.5), and author information. </td>
  </tr>
  <tr>
   <td style="text-align:left;font-weight: bold;width: 10em; "> General </td>
   <td style="text-align:left;font-style: italic;width: 10em; "> _Data and study should be easy to find, and be accessible._ </td>
   <td style="text-align:left;"> Results (including master theses, internal reports, etc.) should be publicly available. Data should be publicly available in a data repository. Funding bodies and journals are increasingly requiring this. Publications should have useful keywords and titles to enable them to be easily found. </td>
  </tr>
</tbody>
</table>



**Study design**

_Study design is reported in sufficient detail_

The description of the study design should be thorough; parts of it can be reported in the appendix if there is limited space. Correctly report:

●   start, end date, and duration of the study

●   treatment factors, levels, and interactions, design structure, e.g. factorial, nested, hierarchical

●   level of replication: number of sites, blocks, plots, and sub-plots; including selection and randomisation process at each level

●   spatial scale: size of the study unit, distance between sites, populations

●   type of data sampled (predictors and covariates), and sampling precision for each (including any within‐replicate sampling or pseudoreplication)

●   sampling schedule: timing, frequency, including study design aspects such as treatment-control, before-after-control-impact, etc. (also see Table 1.1)

●   description of the manipulated organism, population, or community should follow accepted taxonomic literature, e.g. The Plant List (TPL; http://www.theplantlist.org/) and the Taxonomic Name Resolution Service (TNRS; Boyle et al., 2013) and national or international classification schemes.

**Response variables, predictors, and covariates**

_Measurements should be relevant, reproducible, and convertible_

Follow established protocols, and guidance on which and how to measure predictors, response variables, and covariates. Report which protocols are used, and describe any adjustments that are made. Describe all variables fully and report in readme files, data dictionaries, and datasets. Measure useful covariates for synthesis and upscaling (see Table 2 in the main paper).

**Data handling and analysis**

_Data manipulation is described in sufficient detail_ _Comprehensive description of data analysis_       _Reproducible workflow_

Each step of data manipulation should be described and explained and be repeatable and reproducible (British Ecological Society, 2017). Type of statistical tests used, response variables, covariates (explanatory factors) tested, posthoc or planned comparisons carried out, definition of statistical metrics if different from commonly accepted terms should be described. Statistical software, packages, and versions used need to be reported. The workflow from data manipulation, coding, analysing, and results output should be repeatable and reproducible (Lind 2013, British Ecological Society, 2017).

**Results**

_Units need to be reported_ _Raw data should be provided_   _Negative results should be reported_

Units for each variable should be reported. Raw data or summary statistics with mean (or median), variation around the mean and sample size should be reported. Report negative results.





