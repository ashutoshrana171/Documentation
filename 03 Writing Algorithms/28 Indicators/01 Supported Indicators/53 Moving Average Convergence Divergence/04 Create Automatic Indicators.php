<!-- Code generated by Indicator-Reference-Code-Generator.py -->
                        
<? include(DOCS_RESOURCES."/qcalgorithm-api/_method_container.html"); ?>
                        
<p>The MACD method creates an MovingAverageConvergenceDivergence indicator, sets up a consolidator to update the indicator, and then returns the indicator so you can use it in your algorithm.</p>
<p>The following reference table describes the <code>MACD</code> method:</p>

<? include(DOCS_RESOURCES."/qcalgorithm-api/macd.html"); ?>
<br/><? include(DOCS_RESOURCES."/enumerations/moving_average_type.html"); ?>

<p>If you don't provide a resolution, it defaults to the security resolution. If you provide a resolution, it must be greater than or equal to the resolution of the security. For instance, if you subscribe to hourly data for a security, you should update its indicator with data that spans 1 hour or longer.</p>
<p>For more information about the selector argument, see <a href="/docs/v2/writing-algorithms/indicators/automatic-indicators#07-Alternative-Price-Fields">Alternative Price Fields</a>.</p>