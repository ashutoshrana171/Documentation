<p>The <code class="csharp">Leverage</code><code class="python">leverage</code> setting is a <code class='python'>float</code><code class='csharp'>decimal</code> that defines the maximum amount of leverage you can use for a single asset in a non-derivative universe. The default value is <code class="csharp">Security.NullLeverage</code><code class="python">Security.NULL_LEVERAGE</code> (0). To change the leverage, in the <a href='/docs/v2/writing-algorithms/initialization'>Initialize</a> method, adjust the algorithm's <code class="csharp">UniverseSettings</code><code class="python">universe_settings</code> before you
