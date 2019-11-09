---
ID: 416
post_title: >
  5.8 Psychrometry for water potential
  measurements
author: jonathans
post_excerpt: ""
layout: post
permalink: >
  http://climexhandbook.w.uib.no/2019/11/03/psychrometry-for-water-potential-measurements/
published: true
post_date: 2019-11-03 09:00:55
---
<strong>Authors:</strong> Miller ML<sup>1</sup>, Estiarte E<sup>2,3</sup>, Johnson DM<sup>4</sup>, Zinnert J<sup>5</sup>

<strong>Reviewer:</strong> Meinzer F<sup>6</sup>

&nbsp;

<strong>Measurement unit: MPa; Measurement scale: single leaf or stem segment, soil sample; Equipment costs: €€; Running costs: €; Installation effort: medium; Maintenance effort: medium; Knowledge need: medium; Measurement mode: data logger</strong>

Water potential, at its most basic, is a measure of the chemical potential of water within a system as compared to that of pure water (assumed to be 0 MPa at ~ 25 °C) (Tyree &amp; Zimmermann, 2002; Lambers et al., 2008). Plant water potential (Y<sub>w</sub>) has four components: osmotic (Y<sub>p</sub>), matric (Y<sub>m</sub> , hydrostatic pressure (Y<sub>p</sub>), and gravitational (Y<sub>g</sub>) potential (Campbell &amp; Norman, 1998). Matric potential is typically the major component of soil water potential, but it is often ignored in relation to plant material. Likewise, the gravitational component (0.01 MPa m<sup>-1</sup>) is only significant in very tall plant species. Thus, overall plant water potential is generally considered to be Y<sub>w</sub> = Y<sub>p</sub> + Y<sub>p</sub> (Tyree &amp; Zimmermann, 2002; Lambers et al., 2008). Water movement along the soil–plant–atmosphere continuum occurs from compartments of higher to lower Y<sub>w</sub> (less negative to more negative). In living plant tissues, Y<sub>p</sub> is the turgor pressure, whereas in the xylem conduits Y<sub>p</sub> is usually negligible and Y<sub>p</sub> is zero or negative. The ability to accurately measure plant tissue-specific Y<sub>w</sub> in conjunction with other plant physiological properties such as gas exchange or hydraulic conductivity, allows for the evaluation of species’ capacities to function across different ecotones, extreme climate events, and even permits predictions of drought tolerance. Measurements of water potential can prove useful whenever the cycling of water is affected. This is the case in most climate-change studies, but also in studies into effects of other global changes that could alter the water balance, including biodiversity loss or eutrophication.

&nbsp;
<h4><strong>5.8.1 What and how to measure?</strong></h4>
The Scholander-style pressure chamber (PMS Instrument Company) or “pressure bomb” is a standard water potential measurement tool used extensively in plant research (Scholander et al., 1965). However, this approach is limited by the type and size of the plant sample. Water potential measurements on blocks or sections of wood, small tissue samples, or non-woody tissues (i.e. individual small leaves) require an alternative methodology. Thermocouple psychrometry provides a reliable alternative to the pressure bomb.

For thermocouple psychrometry-based water potential measurements of plant tissue, a sample is typically encased in a sealable chamber containing a sample and a reference thermocouple junction. The most common type of thermocouple psychrometer relies on the Peltier effect, whereby an electrical current is briefly passed through the sample thermocouple junction, cooling it below the dew-point temperature of the air in the chamber, causing condensation on the junction (Spanner, 1951). Evaporation of the condensed water upon cessation of cooling creates a temperature depression of the sample junction in comparison to the dry reference junction. This temperature depression and the resulting voltage output (μV) are primarily dependent on the relative humidity inside the chamber. The voltage output can be converted to water potential (MPa) based on the known relationship between vapour pressure (i.e. relative humidity) and water potential in a closed system at a stable temperature. Thus, the water potential of the plant or soil sample is inferred from vapour pressure that is at equilibrium with the sample (Boyer, 1995; Andraski &amp; Scanlon, 2002). Psychrometer chambers are typically connected to a datalogger programmed to provide a specific magnitude and duration of cooling current and to record subsequent microvolt outputs after cooling. A stable thermal environment during psychrometric measurements is crucial because of the exceptionally small temperature differentials and output voltages generated during measurements. Psychrometers have been used for decades to monitor plant and soil water status and the theory behind their operation is discussed extensively in the literature (e.g. Brown &amp; Haveren, 1972; Brown &amp; Bartos, 1982; Boyer, 1995; Marigo &amp; Peltier, 1996; Andraski &amp; Scanlon, 2002; Nobel 2009; Kirkham, 2014).

Prior to use, each thermocouple psychrometer is calibrated against a known set of salt solutions (see below <em>5.8.2 Special cases, emerging issues, and challenges</em>). The thermocouple psychrometers, such as those provided by JRD Merrill Specialty Equipment, are enclosed along with a plant or soil sample, in a stainless-steel chamber (e.g. part 81-500) and then placed into an isothermal environment for equilibration. During equilibration, the datalogger, programmed to convert μV to MPa, takes subsequent measurements at regular intervals (30 minutes to one hour) until the vapour pressure in the chamber equilibrates to the enclosed plant sample. Equilibration can be somewhat arbitrary, but can often take four or more hours and can generally be assumed when two to three subsequent measurements indicate unchanging MPa. The psychrometer-specific calibration factor (see below) is then applied to the datalogger output by the user for a final water potential. Depending on the datalogger manufacturer (see below), calculation of the output water potential from the raw data may be customisable or proprietary. Discussions regarding interpretation can be found in Brown &amp; Bartos (1982) and Andraski &amp; Scanlon (2002).

&nbsp;

<em><strong>Where to start</strong></em>

Amado &amp; Blanco (2004), Andraski &amp; Scanlon (2002), Brown &amp; Bartos (1982), Brown &amp; Haveren (1972), Bulut &amp; Leong (2008)

<strong> </strong>
<h4><em><strong>5.8.2 Special cases, emerging issues, and challenges</strong></em></h4>
<em><strong>System variants</strong></em>

Currently, Campbell Scientific CR6 and CR7 (legacy) dataloggers are commonly used instruments for use with the barrel-style, screen-caged, or end-screen style Peltier psychrometers. The CR6 combined with a multiplexer can support up to 32 individual sensors. The program used with the CR6 is highly modifiable to suit individual needs and the conversion from microvolt (μV) output to water potential (Y<sub>w</sub>), based on Brown &amp; Bartos (1982), is included in the programming. An alternative system, the PsyPro, provides a more user-friendly interface, but is limited in the number of simultaneous measurements (8 sensors) and is not as customisable (see Bulut &amp; Leong 2008, for a more thorough discussion of the pros and cons of the PsyPro and the CR7). Additionally, the PsyPro’s conversion from μV to Y<sub>w</sub> is proprietary. Regardless of datalogger used, sensors need to be calibrated by the user due to minute differences during thermocouple construction, differences between manufacturers, and sensor drift. Brown &amp; Bartos (1982) and Reece (1996) suggest that sensors can be calibrated in batches, where one calibration factor is applied to a subset of all psychrometers. In this configuration, thermocouple psychrometer sensors can be purchased with either a Viking-style connector for easy plug and play connections to dataloggers such as the PsyPro, or without connectors (four-wired) for wiring into Campbell Scientific-style dataloggers. If the psychrometers need to be used with both styles of systems, pigtails can be purchased with the Viking-style connector on one end and 4-wires on the other end, allowing psychrometers purchased with Viking connectors to be used in Campbell Scientific dataloggers.

<em>In situ </em>psychrometric measurements are also possible. For example, ICT International manufactures stem and leaf specific psychrometers and associated dataloggers are designed for application on live (unexcised) plant tissue in field conditions. Additionally, psychrometry can be used for long-term soil monitoring (Andraski &amp; Scanlon, 2002). For soil monitoring, caged-screen or ceramic-bulb sensors are typically inserted directly into the soil rather than enclosing a disturbed soil sample with the thermocouple in a chamber as previously described.

&nbsp;

<em><strong>Calibration</strong></em>

Prior to use, psychrometers, regardless of type or manufacturer, must be calibrated for maximum accuracy. Calibration for the psychrometers is typically performed with a range of known concentrations of salt solutions (KCl or NaCl) with known osmotic potentials (Y<sub>p</sub>  at a given temperature, though care must be taken when mixing solutions regarding molality or osmolality (Tyree &amp; Zimmermann, 2002; Nobel, 2009). While there is no specific recommended number of solutions used or the frequency of calibration, 4–6 solutions are commonly used (Brown &amp; Bartos, 1982; Andraski &amp; Scanlon 2002; Bulut &amp; Leong, 2008). More variability in output has been shown for more negative water potentials and decreased resolution has been illustrated at very high water potentials (near zero), so solutions can be tailored to the expected range of use: a reliable range of psychrometric readings is generally considered to be -0.3 to -7.0 or -8.0 MPa (Andraski &amp; Scanlon 2002; Scanlon et al., 2002; Bulut &amp; Leong 2008). Water potential equivalents for KCl and NaCl can be found throughout the literature including Lang (1967), Brown &amp; Bartos (1982), Bulut &amp; Leong (2008). Water potential can also be calculated based on van’t Hoff’s equation and empirical measurements of the activity coefficients of the respective solution (e.g. Amado &amp; Blanco, 2004). Results of the calibration solutions can be plotted as estimated Y<sub>w</sub> (based on published values per salt solution) as a function of either μV or measured Y<sub>w</sub>, although using μV can be confusing and is best used for troubleshooting purposes only. The resulting linear regression is the psychrometer-specific calibration factor (see Andraski &amp; Scanlon, 2002 for discussion).

The general procedure for calibration is to place a disc of filter paper inside the psychrometer chamber lid or a strip of filter paper around the internal chamber and saturate the disc with a constant volume of salt solution. The psychrometer is then sealed, double bagged in large “ziploc” style 3.75 or 7.5 L bags and placed into a water bath. The sensors are then allowed to equilibrate, where the water potential of the vapour in the chamber equals the water potential (osmotic potential) of the salt solution – generally 30 minutes to 4–6 h is required depending on the concentration of the salt solution and the chamber size. Equilibration is assumed with at least three subsequent consistent measurements.

Psychrometry chambers require regular calibration at a set temperature, and whatever temperature is used for calibration must also be used for sample measurements. The temperature of the water bath is up to the end user, but some practical considerations are advised. For instance, if the water bath is 21 °C, then the temperature control will need to be wired for both heating and cooling. However, if 25 °C is selected, then only the immersion heater will likely be necessary if operated indoors. Additionally, Brown &amp; Bartos (1982) found that 25 °C provided the lowest variability (as compared to 15 and 35 °C) and many of the above references published water potential equivalents of the calibration solutions at 25 °C.

&nbsp;

<em><strong>Environments</strong></em>

While, traditionally, calibration occurs in a temperature-controlled water bath (Brown &amp; Bartos, 1982), an adequate thermal environment can be created in myriad ways. An insulated, non-temperature controlled water bath in a lab environment with relatively stable temperatures provides an adequate psychrometer environment (Andraski &amp; Scanlon, 2002). Lacking ideal thermally-controlled lab settings, an isothermal environment can be created with a modified cooler or high-density Styrofoam with heating and/or cooling and circulation capabilities (e.g. see description in ICT International’s Stem Psychrometer Manual, Ch. 16, http://www.ictinternational.com/support/
product-manuals/). Isothermal conditions cannot be achieved for aboveground and shallow soil <em>in situ</em> sensors, but rapid temperature fluctuations can be minimised by insulating foam and reflective covering for aboveground sensors, and orientation of sensors in shallow soils may minimise temperature gradients (Andraski &amp; Scanlon, 2002). Rawlins &amp; Dalton (1967) have illustrated that major impacts of temperature fluctuations in soil can be largely eliminated.

&nbsp;

<em><strong>Comparing psychrometry results to pressure bomb results</strong></em>

Caution should be exercised in comparing measurements of plant water potential made with psychrometers and the pressure chamber. Although measurements made with the two techniques are often in good agreement, notable discrepancies can occur under certain conditions (e.g. Boyer, 1967; Turner et al., 1984). The presence of native apoplastic solutes is undetectable in pressure chamber measurements, but the influence of these solutes on tissue water potential would be detected in psychrometric measurements. Other sources of discrepancies between the two techniques include an increase in sample turgor, and therefore water potential in the psychrometer chamber resulting from cellular uptake of solutes released from damaged cells, and production of respiratory water during equilibration of tissue in the psychrometer chamber.

&nbsp;

<em><strong>Challenges</strong></em>

Contaminants, including skin oils and residue from evaporated liquids can render measurements unusable. When changing salt solutions or plant samples, all surfaces within the chamber must be cleaned thoroughly to remove contaminates such as particles, plant residues (i.e. sap), and evaporative residues. Additionally, the thermocouple junctions need to be cleaned regularly according to manufacturer’s specifications and subsequently recalibrated. In practice, accurate sensor calibrations and a stable temperature environment are key to accurate psychrometric measurements because the sensor outputs can be highly influenced by temperature gradients.

&nbsp;
<h4><em><strong>5.8.3 References</strong></em></h4>
<em><strong>Theory, significance, and large datasets</strong></em>

<em>Campbell &amp; Gardner (1971), Kirkham (2014), Nobel (2009), Scanlon et al. </em><em>(2002), Spanner (1951)</em>

<em><strong> </strong></em>

<em><strong>More on methods and existing protocols</strong></em>

<em>Lang (1967), Lüttge &amp; Nobel (1984), Marigo &amp; Peltier (1996), Schaefer et al. </em><em>(1986), Touchette (2006)</em>

<em> </em>

<em><strong>All references</strong></em>

Amado, E., &amp; Blanco, L. H. (2004). Osmotic and activity coefficients of aqueous solutions of KCl at temperatures of 283.15, 288.15, 293.15 and 298.15 K: A new isopiestic apparatus. <em>Fluid Phase Equilibria, 226</em>, 261-265.

Andraski, B. J., &amp; Scanlon, B. R. (2002). Thermocouple psychrometry. In J. H. Dan, &amp; C. G. Topp (Eds.), <em>Methods of Soil Analysis: Part 4</em>. Madison: Soil Science Society of America.

Boyer, J. S. (1967). Leaf water potentials measured with a pressure chamber. <em>Plant Physiology</em>, 42(1), 133-137.

Boyer, J. S. (1995). <em>Measuring the Water Status of Plants and Soils</em>. San Diego: Academic Press.

Brown R. W., &amp; Bartos D. L. (1982). A calibration model for screen-caged Peltier thermocouple psychrometers. Research Paper INT-293 USDA Forest Service Intermountain Forest and Range Experiment Station.

Brown, R. W., &amp; Haveren, B. P. V. (1972). Psychrometry in water relations research. In Symposium on Thermocouple Psychrometers (1971: Utah State University). Agricultural Experiment Station.

Bulut R., &amp; Leong E. C. (2008). Indirect measurement of suction. <em>Geotechnical and Geological Engineering, 26</em>, 633-644.

Campbell, G. S., &amp; Gardner, W. H. (1971). Psychrometric measurements of soil water potential: temperature and bulk density effects.  <em>Soil Science Society of America Proceedings, 35</em>, 8-12.

Campbell, G. S., &amp; Norman, J. M. (1998). <em>An Introduction to Environmental Biophysics</em> (2nd ed.). New York: Springer Science &amp; Business Media.

Kirkham, M. B. (2014). Thermocouple psychrometers. In <em>Principles of Soil and Plant Water Relations</em> (2<sup>nd</sup> ed., pp. 311-332). Waltham: Elsevier.

Lambers, H., Chapin, F. S., &amp; Pons, T. L. (2008). <em>Plant Physiological Ecology</em> (2<sup>nd</sup> ed.) New York: Springer.

Lang, A. R. G. (1967). Osmotic coefficients and water potentials of sodium chloride solutions from 0 to 40°C. <em>Australian Journal of Chemistry, 20</em>(9), 2017-2023.

Lüttge, U., &amp; Nobel, P. S. (1984). Day–night variations in malate concentration, osmotic pressure, and hydrostatic pressure in <em>Cereus validus</em>. <em>Plant Physiology</em>, <em>75</em>(3), 804-807.

Marigo G., &amp; Peltier J. P. (1996). Analysis of the diurnal change in osmotic potential in leaves of <em>Fraxinus excelsior</em> L. <em>Journal of Experimental Botany, 47</em>(299), 763-769.

Nobel, P. S. (2009). <em>Physicochemical and Environmental Plant Physiology</em> (4<sup>th</sup> ed.). Oxford: Academic Press.

Rawlins, S. L., &amp; Dalton, F. N. (1967). Psychrometric measurement of soil water potential without precise temperature control. <em>Soil Science Society of America Journal, 31</em>(3), 297-301.

Reece, C. F. (1996). Evaluation of a line heat dissipation sensor for measuring soil matric potential. <em>Soil Science Society of America Journal, 60</em>(4), 1022-1028.

Scanlon, B. R., Andraski, B. J., &amp; Bilskie J. (2002). Miscellaneous methods for measuring matric or water potential. In J. H. Dane, &amp; C. G. Topp (Eds.), <em>Methods of Soil Analysis: Part 4</em> (pp. 643-670). Madison: Soil Science Society of America.

Schaefer, N. L., Trickett, E. S., Ceresa, A., &amp; Barrs, H. D. (1986). Continuous monitoring of plant water potential. <em>Plant Physiology</em>, <em>81</em>(1), 45-49.

Scholander, P. F., Bradstreet, E. D., Hemmingsen, E. A., &amp; Hammel, H. T. (1965). Sap pressure in vascular plants: negative hydrostatic pressure can be measured in plants. <em>Science</em>, <em>148</em>(3668), 339-346.

Spanner, D. C. (1951). The Peltier effect and its use in the measurement of suction pressure. <em>Journal of Experimental Botany</em>, <em>2</em>(5), 145-168.

Touchette, B. W. (2006). Salt tolerance in a <em>Juncus roemerianus</em> brackish marsh: spatial variations in plant water relations. <em>Journal of Experimental Marine Biology and Ecology</em>, <em>337</em>(1), 1-12.

Turner, N. C., Spurway, R. A., &amp; Schulze, E. D. (1984). Comparison of water potentials measured by in situ psychrometry and pressure chamber in morphologically different species. <em>Plant Physiology, 74</em>(2), 316-319.

Tyree, M. T., &amp; Zimmermann, M. H. (2002). <em>Xylem Structure and the Ascent of Sap</em> (2<sup>nd</sup> ed.). Berlin: Springer

<em><strong> </strong></em>

<em><strong> </strong></em>

<strong>Authors:</strong> Miller ML<sup>1</sup>, Estiarte E<sup>2,3</sup>, Johnson DM<sup>4</sup>, Zinnert J<sup>5</sup>

<strong>Reviewer:</strong> Meinzer F<sup>6</sup>

<em><strong> </strong></em>

<em><strong>Affiliations</strong></em>

<sup>1</sup> University of Idaho, College of Natural Resources, Moscow, USA

<sup>2</sup> CSIC, Global Ecology Unit CREAF-CSIC-UAB, Bellaterra, Spain

<sup>3</sup> CREAF, Cerdanyola del Vallès, Spain

<sup>4</sup> Warnell School of Forestry and Natural Resources, University of Georgia, Athens, USA

<sup>5</sup> Department of Biology, Virginia Commonwealth University, Richmond, USA

<sup>6</sup> Pacific Northwest Research Station, USDA Forest Service, Corvallis, USA