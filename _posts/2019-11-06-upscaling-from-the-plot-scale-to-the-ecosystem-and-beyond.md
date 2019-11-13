---
ID: 165
post_title: >
  2.3.3 Upscaling from the plot scale to
  the ecosystem and beyond
author: jonathans
post_excerpt: ""
layout: post
permalink: >
  https://climexhandbook.w.uib.no/2019/11/06/upscaling-from-the-plot-scale-to-the-ecosystem-and-beyond/
published: true
post_date: 2019-11-06 01:00:52
---
<strong>Authors:</strong> Lee H<sup>1</sup>, Vicca S<sup>2</sup>, Stuart-Haëntjens E<sup>3</sup>, Mänd P<sup>4</sup>

<strong>Reviewer:</strong> Gough C<sup>3</sup>

&nbsp;

<strong>Measurement unit: Mg C ha<sup>-1</sup> yr<sup>-1</sup> or Mg C ha<sup>-1</sup>; </strong><strong>Measurement scale: point, plot, ecosystem; Installation costs: €–€€€; Running costs: Not applicable</strong><strong>; Installation effort: medium; Maintenance effort: medium; Knowledge need: medium; Measurement mode: manual or data logger</strong>

As climate change progresses, increasing frequency and severity of extreme events as well as gradual changes in precipitation and temperature regimes threaten terrestrial carbon (C) sinks, making it increasingly important to study ecosystem C stock and C exchange responses to these events (Schwalm et al., 2012; IPCC, 2014). Coupling upscaling techniques with field measurements allows for the extrapolation of biomass, ecosystem C exchange, and photosynthesis data to larger sample areas, eliminating the need for extra time and resources to be spent on collecting additional field data, while also providing a method to monitor less accessible locations (Devagiri et al., 2013; Asner &amp; Mascaro, 2014). The upscaling methods suggested in this protocol can be easily applied to other climate-change drivers as well as any type of ecosystem study that involves measurements at plot scale with broader scale implications. The method in upscaling suggested here applies particularly to ecosystem scale observations such as ecosystem C uptake (ecosystem scale photosynthesis or GPP; ecosystem net primary production or NPP), ecosystem C release (ecosystem respiration or Reco), and net ecosystem C exchange (net ecosystem exchange of C or NEE).

&nbsp;
<h4><strong>2.3.3.1 What and how to measure?</strong></h4>
<strong><em>Upscaling carbon exchange</em></strong>

Ecosystem CO<sub>2</sub> fluxes are most commonly quantified by either the biometric method or the eddy covariance method (see Campioli et al., 2016 and references within for comparison between the two methods). Biometric methods upscale growth and CO<sub>2</sub> flux measurements performed on individual plants or small plots to ecosystem carbon exchange (Cresto Aleina et al., 2016; denoted g C m<sup>−2</sup> y<sup>−1</sup> but more often denoted as mg CO<sub>2</sub> – C m<sup>-2</sup> s<sup>-1</sup>). This is particularly relevant for forests where ecosystem scale flux measurements are only possible with the eddy covariance technique, but the large footprint of the latter usually precludes its use in manipulation experiments (but see e.g. Gough et al., 2013).

Upscaling methods can be classified to data-driven and data-assimilation approaches (see Xiao et al., 2011 and references within). Data-driven approaches are based on empirical, statistical models and are trained with flux observations and various explanatory variables such as land cover, enhanced vegetation index (EVI), photosynthetically active radiation (PAR), land surface temperature, and land surface structure. The empirical models are often a set of multivariate linear submodels under various conditions (rule-based models). Data-assimilation approaches based on simple ecosystem models and parameter estimation techniques, where measurements are used to optimise the parameters of the models, and the optimised models are then used for the estimation of fluxes over broad regions. The Markov chain Monte Carlo (MCMC) and differential evolution (DE) methods can be used in parameter optimisation.

For how to measure biomass, photosynthesis, and carbon fluxes s<a href="https://climexhandbook.w.uib.no/2019/11/06/aboveground-plant-biomass/">ee protocols 2.1.1 Aboveground plant biomass</a>, <a href="https://climexhandbook.w.uib.no/2019/11/06/belowground-plant-biomass/">2.1.2 Belowground plant biomass</a>, <a href="https://climexhandbook.w.uib.no/2019/11/06/leaf-scale-photosynthesis/">2.1.3 Leaf-scale photosynthesis</a> and <a href="https://climexhandbook.w.uib.no/2019/11/06/soil-co2-and-other-trace-gas-fluxes/">2.3.1 Ecosystem CO<sub>2</sub> and trace gas fluxes</a>.

<strong>Measurement unit: Mg C ha<sup>-1</sup> yr<sup>-1</sup>; Equipment costs: €€–€€€; </strong><strong>Running costs: not applicable</strong><strong>; Installation effort: medium; Maintenance effort: medium; Knowledge: medium; Measurement mode: logger or manual</strong>

&nbsp;

<strong><em>Where to start</em></strong>

Campioli et al. (2016), Cresto Aleina et al. (2016), Desai (2010), Lee et al. (2011), Sun et al. (2011)

<strong> </strong>

<strong><em>Upscaling biomass</em></strong>

<strong><em>Gold standard</em></strong>

Lidar, a tool that uses light detection and ranging, is the premier instrument used to quantify and upscale carbon stocks, in part due to vertical height detection (a metric highly correlated with biomass in forested ecosystems) (Chen, 2013). Lidar data are collected via airborne flights (UAV fixed-wing aircrafts) or satellite (upcoming GEDI mission by NASA). To estimate aboveground biomass, height measurements are extracted from the lidar point cloud, paired with ground measurements, and modelled across the whole coverage area (Patenaude et al., 2004). This technique is expensive and airborne lidar surveys are only done on-demand; however, in late 2018, NASA launched GEDI (Global Ecosystem Dynamics Investigation Lidar), a satellite projected to take 15 billion cloud-free observations globally over 24 months. One of their goals is to quantify aboveground biomass, and carbon stocks and flows of forest using a globally consistent data. If resources are limited, NDVI (normalised differential vegetation index) and SAR (synthetic aperture radar) can be extracted from satellite multispectral optical data (see <em>Bronze standard</em>).

&nbsp;

<strong><em>Bronze standard</em></strong>

While some studies upscale using national or continental inventory data (provided by organisations such as the Food and Agriculture Organization of the United Nations (FAO), the Forest Inventory and Analysis (FIA), or the US Department of Agriculture (USDA)), these estimates can exhibit considerable temporal and spatial variation and uncertainty. If lidar data are unobtainable, other remote sensing techniques are available for biomass upscaling including NDVI and SAR (see Devagiri et al., 2013; Laurin et al., 2017). These data products are openly available and can be accessed using NASA’s MODIS (Moderate Resolution Imaging Spectroradiometer) website.

<strong>Measurement unit: Mg C ha<sup>-1</sup>; Equipment costs: €–€€€; </strong><strong>Running costs: not applicable</strong><strong>; Installation effort: medium; Maintenance effort: medium; Knowledge: medium; Measurement mode: logger or manual </strong>

&nbsp;

<strong><em>Where to start</em></strong>

Asner &amp; Mascaro (2014), Chen (2013), Devagiri et al. (2013), Laurin et al. (2017), Patenaude et al. (2004)

&nbsp;

<strong><em>Upscaling photosynthesis</em></strong>

<strong><em>Gold standard</em></strong>

Two main process-based model types are used for upscaling photosynthesis to ecosystem level: “big leaf” models and two-leaf models. The “big leaf” principle (Farquhar et al., 1980, Farquhar &amp; von Caemmerer, 1982) is most commonly used in ecosystem models and assumes that canopy photosynthesis responds similarly to a single unshaded canopy leaf, where chloroplasts acclimate to the within-leaf light profile. However, total canopy photosynthesis often varies from up-scaled single-leaf derivations due to canopy light level complexity caused by sun flecks, leaf angle variation, and canopy clumping (Kull, 2002). This underestimation becomes especially evident in structurally complex systems (such as forests). The two-leaf models divide canopies into sunlit and shaded sections, or in more complex models, divide canopies into several layers and incorporate leaf angle (de Pury &amp; Farquhar, 1997). Two-leaf models appear to represent photosynthesis more adequately in more complex environments (Mercado et al., 2009; Sprintsin et al., 2012).

Measuring large-scale photosynthesis as gross primary production (GPP):
<ol>
 	<li>In more simple ecosystems (grasslands, shrublands), canopy gas-exchange chambers can be used for estimations of photosynthesis (<a href="https://climexhandbook.w.uib.no/2019/11/06/ecosystem-co2-and-trace-gas-fluxes/">see protocol 3.3.1 Ecosystem CO<sub>2</sub> and trace gas fluxes</a>).</li>
 	<li>For more complex systems, such as forests, eddy-covariance data can be used (<a href="https://climexhandbook.w.uib.no/2019/11/06/ecosystem-co2-and-trace-gas-fluxes/">see protocol 3.3.1 Ecosystem CO<sub>2</sub> and trace gas fluxes</a>) but this cannot be used for small treatment plots.</li>
 	<li>A third possibility is to measure canopy reflectance from above the plant canopy (<a href="https://climexhandbook.w.uib.no/2019/11/03/reflectance-assessment-of-plant-physiological-status/">see protocol 5.12 Reflectance assessments of plant physiological status</a>). Different reflectance indices, such as PRI and others have been shown to correlate with leaf-level photochemical efficiency of plants (Gamon et al., 1992; Garbulsky et al., 2013), however ecosystem structure strongly affects the use of reflectance indices for photosynthesis estimations (Mänd et al., 2010; Vicca et al., 2016). For larger areas, it might be possible to use already available reflectance data (e.g. data acquired by satellite-born MODerate resolution Imaging Spectrometer – MODIS, NASA), but this is not possible for small plots.</li>
</ol>
&nbsp;

<strong><em>Bronze standard</em></strong>

If direct measurements of leaf photosynthetic capacity are not possible, databases of species-specific maximal photosynthetic capacity can be used for model parametrisation (<a href="https://daac.ornl.gov/VEGETATION/guides/Leaf_Photosynthesis_Traits.html">https://daac.ornl.gov/VEGETATION/guides/Leaf_Photosynthesis_Traits.html</a>), but it should be noted that photosynthesis is likely to be altered in climate-manipulation experiments.

&nbsp;

<strong><em>Where to start</em></strong>

Farquhar et al. (1980), Sprintsin et al. (2012)

&nbsp;

<strong>2.3.3.3 References</strong>

<strong><em>Theory, significance, and large datasets</em></strong>

Farquhar &amp; von Caemmerer (1982), Jung et al. (2011), Xiao et al. (2011)

&nbsp;

<strong><em>More on methods and existing protocols</em></strong>

Asner &amp; Mascaro (2014), Campiol et al. (2016), Jung et al. (2011), Xiao et al. (2011)

&nbsp;

<strong><em>All references</em></strong>

Asner, G.P., &amp; Mascaro, J. (2014). Mapping tropical forest carbon: calibrating plot estimates to a simple LiDAR metric. <em>Remote Sensing of Environment, 140</em>, 614-624.

Campioli, M., Malhi, Y., Vicca, S., Luyssaert, S., Papale, D., Peñuelas, J., … Janssens, I.A. (2016). Evaluating the convergence between eddy-covariance and biometric methods for assessing carbon budgets of forests. <em>Nature Communications, 7</em>, art13717.

Chen, Q. (2013). Lidar remote sensing of vegetation biomass. <em>Remote Sensing of Natural Resources, 399</em>, 399-420.

Cresto Aleina, F., Runkle, B. R. K., Brücher, T., Kleinen, T., &amp; Brovkin, V. (2016). Upscaling methane emission hotspots in boreal peatlands. <em>Geoscience Model Development, 9</em>, 915-926.

de Pury, D. D., &amp; Farquhar, G. D. (1997). Simple scaling of photosynthesis from leaves to canopies without the errors of big‐leaf models. <em>Plant, Cell &amp; Environment</em>, <em>20</em>(5), 537-557.

Desai, A. R. (2010), Climatic and phenological controls on coherent regional interannual variability of carbon dioxide flux in a heterogeneous landscape. <em>Journal of Geophysical Research, 115</em>, G00J02.

Devagiri, G. M., Money, S., Singh, S., Dadhawal, V. K., Patil, P., Khaple, A., … Hubballi, S. (2013). Assessment of above ground biomass and carbon pool in different vegetation types of south western part of Karnataka, India using spectral modeling. <em>Tropical Ecology, 54</em>(2), 149-165.

Farquhar, G. D., &amp; von Caemmerer, S. (1982). Modelling of photosynthetic response to environmental conditions. In O. L. Lange, P. S. Nobel, C. B. Osmond, &amp; H. Ziegler (Eds.), <em>Physiological Plant Ecology II</em> (pp. 549-587). Berlin: Springer.

Farquhar, G. D., von Caemmerer, S., &amp; Berry, J. A. (1980). A biochemical model of photosynthetic CO<sub>2</sub> assimilation in leaves of C<sub>3</sub> species. <em>Planta</em>, <em>149</em>(1), 78-90.

Gamon, J. A., Peñuelas, J., &amp; Field, C. B. (1992). A narrow-waveband spectral index that tracks diurnal changes in photosynthetic efficiency. <em>Remote Sensing of Environment</em>, <em>41</em>(1), 35-44.

Garbulsky, M. F., Peñuelas, J., Ogaya, R., &amp; Filella, I. (2013). Leaf and stand-level carbon uptake of a Mediterranean forest estimated using the satellite-derived reflectance indices EVI and PRI. <em>International Journal of Remote Sensing</em>, <em>34</em>(4), 1282-1296

Gough, C. M., Hardiman, B. S., Nave, L. E.,  Bohrer, G., Maurer, K. D., Vogel, C. S., … Curtis, P. S. (2013). Sustained carbon uptake and storage following moderate disturbance in a Great Lakes forest. <em>Ecological Applications, 23</em>, 12012-1215.

IPCC (2014). <em>Climate Change 2014: Impacts, Adaptation, and Vulnerability. Part A: Global and Sectoral Aspects. Contribution of Working Group II to the Fifth Assessment Report of the Intergovernmental Panel on Climate Change</em>. Cambridge: Cambridge University Press

Jung, M., Reichstein, M., Margolis, H. A., Cescatti, A., Richardson, A. D., Arain, M. A., … Williams, C. (2011). Global patterns of land-atmosphere fluxes of carbon dioxide, latent heat, and sensible heat derived from eddy covariance, satellite, and meteorological observations. <em>Journal of Geophysical Research, 116</em>, G00J07.

Kull, O. (2002). Acclimation of photosynthesis in canopies: models and limitations. <em>Oecologia</em>, <em>133</em>(3), 267-279.

Laurin, G. A., Pirotti, F., Callegari, M., Chen, Q., Cuozzo, G., Lingua, E., … Papale, D. (2017). Potential of ALOS2 and NDVI to estimate forest above-ground biomass, and comparison with lidar-derived estimates. <em>Remote Sensing, 9</em>(1), 18.

Lee H., Schuur E. A. G., Vogel J. G., Lavoie M., Bhadra D., &amp; Staudhammer C.L. (2011). A spatially explicit analysis to extrapolate carbon fluxes in upland tundra where permafrost is thawing. <em>Global Change Biology, 17</em>, 1379-1393.

Mänd, P., Hallik, L., Peñuelas, J., Nilson, T., Duce, P., Emmett, B. A., ... Schmidt, I. K. (2010). Responses of the reflectance indices PRI and NDVI to experimental warming and drought in European shrublands along a north–south climatic gradient. <em>Remote Sensing of Environment</em>, <em>114</em>(3), 626-636.

Mercado, L. M., Lloyd, J., Dolman, A. J., Sitch, S., &amp; Patino, S. (2009). Modelling basin-wide variations in Amazon forest productivity–Part 1: Model calibration, evaluation and upscaling functions for canopy photosynthesis. <em>Biogeosciences</em>, <em>6</em>(7), 1247-1272.

Patenaude, G., Hill, R. A., Milne, R., Gaveau, D. L. A., Briggs, B. B. J., &amp; Dawson, T. P. (2004). Quantifying forest above ground carbon content using LiDAR remote sensing. <em>Remote Sensing of Environment, 93</em>, 368-380.

Schwalm, C. R., Williams, C. A., Schaefer, K., Baldocci D., Black, A., Goldstein A. H., … Scott, R. L. (2012). Reduction in carbon uptake during turn of the century drought in western North America. <em>Nature Geoscience, 5</em>, 551-556.

Sprintsin, M., Chen, J. M., Desai, A., &amp; Gough, C. M. (2012). Evaluation of leaf‐to‐canopy upscaling methodologies against carbon flux data in North America. <em>Journal of Geophysical Research: Biogeosciences</em>, <em>117</em>(G1), G01023.

Sun, G., Caldwell, P., Noormets, A., McNulty, S. G., Cohen, E., Moore Myers, J., … Chen, J. (2011), Upscaling key ecosystem functions across the conterminous United States by a water-centric ecosystem model. <em>Journal of Geophysical Research, 116</em>, G00J05.

Vicca, S., Balzarolo, M., Filella, I., Granier, A., Herbst, M., Knohl, A., ... Rambal, S. (2016). Remotely-sensed detection of effects of extreme droughts on gross primary production. <em>Scientific Reports</em>, <em>6</em>, 28269.

Xiao, J., Davis, K. J., Urban, N. M., Keller, K., &amp; Saliendra, N. Z. (2011). Upscaling carbon fluxes from towers to the regional scale: Influence of parameter variability and land cover representation on regional flux estimates. <em>Journal of Geophysical Research,</em> <em>116</em>, G00J06.

&nbsp;

&nbsp;

<strong>Authors:</strong> Lee H<sup>1</sup>, Vicca S<sup>2</sup>, Stuart-Haëntjens E<sup>3</sup>, Mänd P<sup>4</sup>

<strong>Reviewer:</strong> Gough C<sup>3</sup>

<strong> </strong>

<strong>Affiliations</strong>

<sup>1</sup> NORCE Norwegian Research Centre and Bjerknes Centre for Climate Research, Bergen, Norway

<sup>2</sup> Centre of Excellence PLECO (Plants and Ecosystems), Biology Department, University of Antwerp, Wilrijk, Belgium

<sup>3</sup> Department of Biology, Virginia Commonwealth University, Richmond, USA

<sup>4</sup> Institute of Ecology and Earth Sciences, University of Tartu, Tartu, Estonia