class Linguagens:
	def __init__(self, linguagem, idioma):
		self.name = linguagem
		self.age = idioma

	def reduc_ptbr_parte1(self):
		parte1="""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<!DOCTYPE language SYSTEM \"language.dtd\"
[
	<!ENTITY int \"(?:[0-9]++)\">
	<!ENTITY hex_int \"(?:[0-9A-Fa-f]++)\">
	<!ENTITY exp_float \"(?:[eE][+-]?&int;)\">
	<!ENTITY exp_hexfloat \"(?:[pP][-+]?&int;)\">

	<!ENTITY ispphash \"(?:#|&#37;\:|\?\?=)\">
	<!ENTITY pphash \"&ispphash;\s*\">
]>
<language name=\"R-EDUC\" section="Sources"
		version=\"11\" kateversion="5.0"
		indenter=\"cstyle\"
		extensions=\"*.sBoticsR\"
		mimetype=\"text/x-reduc\"
		priority=\"5\">
<!--

	Editado por Francisco Iago Lira Passos (iagolirapassos@gmail.com)

	NOTE: Usar com R-EDUC (.sBoticsR)

	Version 1
-->
<highlighting>
	<list name=\"controlflow\">
	<item>interromper</item>
	<item>outros</item>
	<item>farei</item>
	<item>enquanto</item>
	<item>farei</item>
	<item>repita</item>
	<item>vezes</item>
	<item>para</item>
	<item>de</item>
	<item>ate</item>
	<item>passo</item>
	<item>farei</item>
	<item>teste</item>
	<item>caso</item>
	<item>outros</item>
	<item>se</item>
	<item>entao</item>
	<item>senao</item>
	<item>interromper</item>
  <item>tarefa</item>
	<item>inicio</item>
	<item>fim</item>
	</list>
			"""
		return parte1

	def reduc_ptbr_parte3(self):
		parte3 = """
<list name="types">
      <item>numero</item>
      <item>texto</item>
      <item>booleano</item>
    </list>
    <contexts>
      <context attribute="Normal Text" lineEndContext="#stay" name="Normal">
        <DetectSpaces />
        <RegExpr attribute="Preprocessor" context="Outscoped" String="&pphash;if\s+0\s*$" beginRegion="PP" firstNonSpace="true" />
        <RegExpr context="AfterHash" String="&ispphash;" firstNonSpace="false" lookAhead="false" />
        <keyword attribute="Control Flow" context="#stay" String="controlflow"/>
        <keyword attribute="Keyword" context="#stay" String="keywords"/>
        <keyword attribute="Data Type" context="#stay" String="types"/>
        <DetectIdentifier />
        <DetectChar attribute="Symbol" context="#stay" char="{" beginRegion="Brace1" />
        <DetectChar attribute="Symbol" context="#stay" char="}" endRegion="Brace1" />

        <RegExpr attribute="Decimal" context="Number" String="\.?[0-9]" lookAhead="true" />
				<RegExpr attribute="int" context="Number" String="&beforeDigit;(?:[1-9](?:_?\d)*|0(?:_?0)*)[lL]?\b" context="#stay"/>

        <HlCChar attribute="Char" context="#stay"/>
        <DetectChar attribute="String" context="String" char="&quot;"/>
        <IncludeRules context="FindComments" />
        <AnyChar attribute="Symbol" context="#stay" String=":!%&amp;()+,-/.*&lt;=&gt;?[]|~^&#59;"/>
      </context>

      <context attribute="String" lineEndContext="#pop" name="String">
        <LineContinue attribute="String" context="#stay"/>
        <HlCStringChar attribute="String Char" context="#stay"/>
        <DetectChar attribute="String" context="#pop" char="&quot;"/>
      </context>

      <context name="FindComments" attribute="Normal Text" lineEndContext="#pop">
				<DetectChar attribute="Comment" char="#" context="MatchComment"/>
        <Detect2Chars attribute="Comment" context="MatchComment" char="(" char1=")" lookAhead="true" />
      </context>

      <context name="MatchComment" attribute="Normal Text" lineEndContext="#pop" fallthrough="true" fallthroughContext="#pop">
        <StringDetect attribute="Region Marker" context="#pop!Region Marker" String="//BEGIN" beginRegion="Region1" firstNonSpace="true" />
        <StringDetect attribute="Region Marker" context="#pop!Region Marker" String="//END" endRegion="Region1" firstNonSpace="true" />
        <IncludeRules context="##Doxygen" />
				<DetectChar attribute="Comment" char="#" context="#pop!Commentar 2"/>
      </context>

      <context attribute="Region Marker" lineEndContext="#pop" name="Region Marker">
      </context>

      <context attribute="Comment" lineEndContext="#pop" name="Commentar 1">
        <LineContinue attribute="Comment" context="#stay"/>
        <IncludeRules context="##Alerts" />
        <IncludeRules context="##Modelines" />
      </context>

      <context attribute="Comment" lineEndContext="#stay" name="Commentar 2">
				<DetectChar attribute="Comment" char="#" context="#stay"/>
        <IncludeRules context="##Alerts" />
        <IncludeRules context="##Modelines" />
      </context>
      
      <context attribute="Error" lineEndContext="#pop" name="AfterHash">
        <RegExpr attribute="Preprocessor" context="Include" String="&pphash;(?:include|include_next)" insensitive="true" firstNonSpace="true" />

        <!-- define, elif, else, endif, error, if, ifdef, ifndef, line, pragma, undef, warning -->
        <RegExpr attribute="Preprocessor" context="Preprocessor" String="&pphash;if(?:def|ndef)?(?=\s+\S)" insensitive="true" beginRegion="PP" firstNonSpace="true" />
        <RegExpr attribute="Preprocessor" context="Preprocessor" String="&pphash;endif" insensitive="true" endRegion="PP" firstNonSpace="true" />
        <RegExpr attribute="Preprocessor" context="Define" String="&pphash;define.*((?=\\))" insensitive="true" firstNonSpace="true" />

        <!-- folding for apple style #pragma mark - label -->
        <RegExpr attribute="Preprocessor" context="Preprocessor" String="&pphash;pragma\s+mark\s+-\s*$" insensitive="true" firstNonSpace="true" endRegion="pragma_mark" />
        <RegExpr attribute="Preprocessor" context="Preprocessor" String="&pphash;pragma\s+mark" insensitive="true" firstNonSpace="true" endRegion="pragma_mark" beginRegion="pragma_mark" />

        <RegExpr attribute="Preprocessor" context="Preprocessor" String="&pphash;(?:el(?:se|if)|define|undef|line|error|warning|pragma)" insensitive="true" firstNonSpace="true" />
        <RegExpr attribute="Preprocessor" context="Preprocessor" String="&ispphash;\s+[0-9]+" insensitive="true" firstNonSpace="true" />
      </context>

      <context attribute="Preprocessor" lineEndContext="#pop" name="Include">
        <LineContinue attribute="Preprocessor" context="#stay"/>
        <RangeDetect attribute="Prep. Lib" context="#stay" char="&quot;" char1="&quot;"/>
        <RangeDetect attribute="Prep. Lib" context="#stay" char="&lt;" char1="&gt;"/>
        <IncludeRules context="Preprocessor" />
      </context>

      <context attribute="Preprocessor" lineEndContext="#pop" name="Preprocessor">
        <LineContinue attribute="Preprocessor" context="#stay"/>
        <IncludeRules context="FindComments" />
      </context>

      <context attribute="Preprocessor" lineEndContext="#pop" name="Define">
        <LineContinue attribute="Preprocessor" context="#stay"/>
      </context>

			<!-- Comments -->

      <context attribute="Comment" lineEndContext="#stay" name="Outscoped" >
        <DetectSpaces />
        <IncludeRules context="##Alerts" />
        <DetectIdentifier />
        <IncludeRules context="FindComments" />
        <RegExpr attribute="Comment" context="Outscoped intern" String="&pphash;if" beginRegion="PP" firstNonSpace="true" />
        <RegExpr attribute="Preprocessor" context="#pop" String="&pphash;el(?:se|if)" firstNonSpace="true" />
        <RegExpr attribute="Preprocessor" context="#pop" String="&pphash;endif" endRegion="PP" firstNonSpace="true" />
        <DetectChar attribute="String" context="String" char="#"/>
      </context>

      <context attribute="Comment" lineEndContext="#stay" name="Outscoped intern">
        <DetectSpaces />
        <IncludeRules context="##Alerts" />
        <DetectIdentifier />
        <IncludeRules context="FindComments" />
        <RegExpr attribute="Comment" context="#pop" String="#"/>
        <RegExpr attribute="Comment" context="#pop" String="&pphash;endif" endRegion="PP" firstNonSpace="true" />
        <DetectChar attribute="String" context="String" char="#"/>
      </context>

      <context name="Number" attribute="Normal Text" lineEndContext="#pop" fallthrough="true" fallthroughContext="#pop">
        <RegExpr attribute="Float" context="FloatSuffix" String="\.&int;&exp_float;?|0[xX](?:\.&hex_int;&exp_hexfloat;?|&hex_int;(?:&exp_hexfloat;|\.&hex_int;?&exp_hexfloat;?))|&int;(?:&exp_float;|\.&int;?&exp_float;?)" />
        <IncludeRules context="Integer" />
      </context>

      <context name="Integer" attribute="Normal Text" lineEndContext="#pop" fallthrough="true" fallthroughContext="#pop">
        <RegExpr attribute="Hex" context="IntSuffix" String="0[xX]&hex_int;" />
        <RegExpr attribute="Binary" context="IntSuffix" String="0[Bb][01]++" />
        <RegExpr attribute="Octal" context="IntSuffix" String="0[0-7]++" />
        <RegExpr attribute="int" context="IntSuffix" String="0(?![xXbB0-9])|[1-9][0-9]*+" />
        <RegExpr attribute="Error" context="#pop" String="[._0-9A-Za-z']++" />
      </context>

      <context name="IntSuffix" attribute="Error" lineEndContext="#pop#pop" fallthrough="true" fallthroughContext="NumericSuffixError">
        <DetectChar attribute="Error" context="#stay" char="'" />
        <AnyChar attribute="Error" context="#pop!IntSuffixPattern" String="uUlLimunshyd_" lookAhead="true" />
      </context>

      <context name="IntSuffixPattern" attribute="Error" lineEndContext="#pop#pop" fallthrough="true" fallthroughContext="NumericSuffixError">
        <RegExpr attribute="Standard Suffix" context="NumericSuffixError" String="[Uu][Ll]{0,2}|[Ll]{0,2}[Uu]?" />
      </context>

      <context name="FloatSuffix" attribute="Error" lineEndContext="#pop#pop" fallthrough="true" fallthroughContext="NumericSuffixError">
        <AnyChar attribute="Standard Suffix" context="NumericSuffixError" String="fFlL" />
      </context>

      <context name="NumericSuffixError" attribute="Error" lineEndContext="#pop#pop#pop" fallthrough="true" fallthroughContext="#pop#pop#pop">
        <RegExpr attribute="Error" context="#pop#pop#pop" String="\.[_0-9A-Za-z]*|[_0-9A-Za-z]+" />
      </context>
    </contexts>
    <itemDatas>
			<itemData name="Normal Text"  defStyleNum="dsNormal" spellChecking="false"/>
      <itemData name="Control Flow" defStyleNum="dsControlFlow" spellChecking="false"/>
      <itemData name="Keyword"      defStyleNum="dsKeyword" spellChecking="false"/>
      <itemData name="Data Type"    defStyleNum="dsDataType" spellChecking="false"/>
      <itemData name="Float"      defStyleNum="dsFloat" spellChecking="false"/>
      <itemData name="int"      defStyleNum="dsDecVal" spellChecking="false"/>
      <itemData name="Standard Suffix" defStyleNum="dsBuiltIn" spellChecking="false" />
      <itemData name="Char"         defStyleNum="dsChar" spellChecking="false"/>
      <itemData name="String"       defStyleNum="dsString"/>
      <itemData name="String Char"  defStyleNum="dsSpecialChar"/>
      <itemData name="Comment"      defStyleNum="dsComment"/>
      <itemData name="Symbol"       defStyleNum="dsOperator" spellChecking="false"/>
      <itemData name="Preprocessor" defStyleNum="dsPreprocessor" spellChecking="false"/>
      <itemData name="Prep. Lib"    defStyleNum="dsImport" spellChecking="false"/>
      <itemData name="Region Marker" defStyleNum="dsRegionMarker" spellChecking="false"/>
    </itemDatas>
  </highlighting>
  <general>
    <comments>
      <comment name="singleLine" start="#" position="afterwhitespace"/>
    </comments>
		<keywords casesensitive="1" additionalDeliminator="#'"/>
  </general>
</language>
<!-- kate: replace-tabs on; tab-width 2; indent-width 2; -->		
		"""
		return parte3

	def reduc_en_parte1(self):
		parte1="""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<!DOCTYPE language SYSTEM \"language.dtd\"
[
	<!ENTITY int \"(?:[0-9]++)\">
	<!ENTITY hex_int \"(?:[0-9A-Fa-f]++)\">
	<!ENTITY exp_float \"(?:[eE][+-]?&int;)\">
	<!ENTITY exp_hexfloat \"(?:[pP][-+]?&int;)\">

	<!ENTITY ispphash \"(?:#|&#37;\:|\?\?=)\">
	<!ENTITY pphash \"&ispphash;\s*\">
]>
<language name=\"R-EDUC\" section="Sources"
		version=\"11\" kateversion="5.0"
		indenter=\"cstyle\"
		extensions=\"*.sBoticsR\"
		mimetype=\"text/x-reduc\"
		priority=\"5\">
<!--

	Editado por Francisco Iago Lira Passos (iagolirapassos@gmail.com)

	NOTE: Usar com R-EDUC (.sBoticsR)

	Version 1
-->
<highlighting>
	<list name=\"controlflow\">
	<item>breakLoop</item>
	<item>others</item>
	<item>while</item>
	<item>repeat</item>
	<item>times</item>
	<item>for</item>
	<item>of</item>
	<item>until</item>
	<item>step</item>
	<item>do</item>
	<item>test</item>
	<item>caso</item>
	<item>if</item>
	<item>then</item>
	<item>else</item>
	<item>true</item>
	<item>false</item>
	<item>and</item>
	<item>true</item>
	<item>begin</item>
	<item>end</item>
	</list>
			"""
		return parte1

	def reduc_en_parte3(self):
		parte3 = """
<list name="types">
      <item>numero</item>
      <item>texto</item>
      <item>booleano</item>
    </list>
    <contexts>
      <context attribute="Normal Text" lineEndContext="#stay" name="Normal">
        <DetectSpaces />
        <RegExpr attribute="Preprocessor" context="Outscoped" String="&pphash;if\s+0\s*$" beginRegion="PP" firstNonSpace="true" />
        <RegExpr context="AfterHash" String="&ispphash;" firstNonSpace="false" lookAhead="false" />
        <keyword attribute="Control Flow" context="#stay" String="controlflow"/>
        <keyword attribute="Keyword" context="#stay" String="keywords"/>
        <keyword attribute="Data Type" context="#stay" String="types"/>
        <DetectIdentifier />
        <DetectChar attribute="Symbol" context="#stay" char="{" beginRegion="Brace1" />
        <DetectChar attribute="Symbol" context="#stay" char="}" endRegion="Brace1" />

        <RegExpr attribute="Decimal" context="Number" String="\.?[0-9]" lookAhead="true" />
				<RegExpr attribute="int" context="Number" String="&beforeDigit;(?:[1-9](?:_?\d)*|0(?:_?0)*)[lL]?\b" context="#stay"/>

        <HlCChar attribute="Char" context="#stay"/>
        <DetectChar attribute="String" context="String" char="&quot;"/>
        <IncludeRules context="FindComments" />
        <AnyChar attribute="Symbol" context="#stay" String=":!%&amp;()+,-/.*&lt;=&gt;?[]|~^&#59;"/>
      </context>

      <context attribute="String" lineEndContext="#pop" name="String">
        <LineContinue attribute="String" context="#stay"/>
        <HlCStringChar attribute="String Char" context="#stay"/>
        <DetectChar attribute="String" context="#pop" char="&quot;"/>
      </context>

      <context name="FindComments" attribute="Normal Text" lineEndContext="#pop">
				<DetectChar attribute="Comment" char="#" context="MatchComment"/>
        <Detect2Chars attribute="Comment" context="MatchComment" char="(" char1=")" lookAhead="true" />
      </context>

      <context name="MatchComment" attribute="Normal Text" lineEndContext="#pop" fallthrough="true" fallthroughContext="#pop">
        <StringDetect attribute="Region Marker" context="#pop!Region Marker" String="//BEGIN" beginRegion="Region1" firstNonSpace="true" />
        <StringDetect attribute="Region Marker" context="#pop!Region Marker" String="//END" endRegion="Region1" firstNonSpace="true" />
        <IncludeRules context="##Doxygen" />
				<DetectChar attribute="Comment" char="#" context="#pop!Commentar 2"/>
      </context>

      <context attribute="Region Marker" lineEndContext="#pop" name="Region Marker">
      </context>

      <context attribute="Comment" lineEndContext="#pop" name="Commentar 1">
        <LineContinue attribute="Comment" context="#stay"/>
        <IncludeRules context="##Alerts" />
        <IncludeRules context="##Modelines" />
      </context>

      <context attribute="Comment" lineEndContext="#stay" name="Commentar 2">
				<DetectChar attribute="Comment" char="#" context="#stay"/>
        <IncludeRules context="##Alerts" />
        <IncludeRules context="##Modelines" />
      </context>
      
      <context attribute="Error" lineEndContext="#pop" name="AfterHash">
        <RegExpr attribute="Preprocessor" context="Include" String="&pphash;(?:include|include_next)" insensitive="true" firstNonSpace="true" />

        <!-- define, elif, else, endif, error, if, ifdef, ifndef, line, pragma, undef, warning -->
        <RegExpr attribute="Preprocessor" context="Preprocessor" String="&pphash;if(?:def|ndef)?(?=\s+\S)" insensitive="true" beginRegion="PP" firstNonSpace="true" />
        <RegExpr attribute="Preprocessor" context="Preprocessor" String="&pphash;endif" insensitive="true" endRegion="PP" firstNonSpace="true" />
        <RegExpr attribute="Preprocessor" context="Define" String="&pphash;define.*((?=\\))" insensitive="true" firstNonSpace="true" />

        <!-- folding for apple style #pragma mark - label -->
        <RegExpr attribute="Preprocessor" context="Preprocessor" String="&pphash;pragma\s+mark\s+-\s*$" insensitive="true" firstNonSpace="true" endRegion="pragma_mark" />
        <RegExpr attribute="Preprocessor" context="Preprocessor" String="&pphash;pragma\s+mark" insensitive="true" firstNonSpace="true" endRegion="pragma_mark" beginRegion="pragma_mark" />

        <RegExpr attribute="Preprocessor" context="Preprocessor" String="&pphash;(?:el(?:se|if)|define|undef|line|error|warning|pragma)" insensitive="true" firstNonSpace="true" />
        <RegExpr attribute="Preprocessor" context="Preprocessor" String="&ispphash;\s+[0-9]+" insensitive="true" firstNonSpace="true" />
      </context>

      <context attribute="Preprocessor" lineEndContext="#pop" name="Include">
        <LineContinue attribute="Preprocessor" context="#stay"/>
        <RangeDetect attribute="Prep. Lib" context="#stay" char="&quot;" char1="&quot;"/>
        <RangeDetect attribute="Prep. Lib" context="#stay" char="&lt;" char1="&gt;"/>
        <IncludeRules context="Preprocessor" />
      </context>

      <context attribute="Preprocessor" lineEndContext="#pop" name="Preprocessor">
        <LineContinue attribute="Preprocessor" context="#stay"/>
        <IncludeRules context="FindComments" />
      </context>

      <context attribute="Preprocessor" lineEndContext="#pop" name="Define">
        <LineContinue attribute="Preprocessor" context="#stay"/>
      </context>

			<!-- Comments -->

      <context attribute="Comment" lineEndContext="#stay" name="Outscoped" >
        <DetectSpaces />
        <IncludeRules context="##Alerts" />
        <DetectIdentifier />
        <IncludeRules context="FindComments" />
        <RegExpr attribute="Comment" context="Outscoped intern" String="&pphash;if" beginRegion="PP" firstNonSpace="true" />
        <RegExpr attribute="Preprocessor" context="#pop" String="&pphash;el(?:se|if)" firstNonSpace="true" />
        <RegExpr attribute="Preprocessor" context="#pop" String="&pphash;endif" endRegion="PP" firstNonSpace="true" />
        <DetectChar attribute="String" context="String" char="#"/>
      </context>

      <context attribute="Comment" lineEndContext="#stay" name="Outscoped intern">
        <DetectSpaces />
        <IncludeRules context="##Alerts" />
        <DetectIdentifier />
        <IncludeRules context="FindComments" />
        <RegExpr attribute="Comment" context="#pop" String="#"/>
        <RegExpr attribute="Comment" context="#pop" String="&pphash;endif" endRegion="PP" firstNonSpace="true" />
        <DetectChar attribute="String" context="String" char="#"/>
      </context>

      <context name="Number" attribute="Normal Text" lineEndContext="#pop" fallthrough="true" fallthroughContext="#pop">
        <RegExpr attribute="Float" context="FloatSuffix" String="\.&int;&exp_float;?|0[xX](?:\.&hex_int;&exp_hexfloat;?|&hex_int;(?:&exp_hexfloat;|\.&hex_int;?&exp_hexfloat;?))|&int;(?:&exp_float;|\.&int;?&exp_float;?)" />
        <IncludeRules context="Integer" />
      </context>

      <context name="Integer" attribute="Normal Text" lineEndContext="#pop" fallthrough="true" fallthroughContext="#pop">
        <RegExpr attribute="Hex" context="IntSuffix" String="0[xX]&hex_int;" />
        <RegExpr attribute="Binary" context="IntSuffix" String="0[Bb][01]++" />
        <RegExpr attribute="Octal" context="IntSuffix" String="0[0-7]++" />
        <RegExpr attribute="int" context="IntSuffix" String="0(?![xXbB0-9])|[1-9][0-9]*+" />
        <RegExpr attribute="Error" context="#pop" String="[._0-9A-Za-z']++" />
      </context>

      <context name="IntSuffix" attribute="Error" lineEndContext="#pop#pop" fallthrough="true" fallthroughContext="NumericSuffixError">
        <DetectChar attribute="Error" context="#stay" char="'" />
        <AnyChar attribute="Error" context="#pop!IntSuffixPattern" String="uUlLimunshyd_" lookAhead="true" />
      </context>

      <context name="IntSuffixPattern" attribute="Error" lineEndContext="#pop#pop" fallthrough="true" fallthroughContext="NumericSuffixError">
        <RegExpr attribute="Standard Suffix" context="NumericSuffixError" String="[Uu][Ll]{0,2}|[Ll]{0,2}[Uu]?" />
      </context>

      <context name="FloatSuffix" attribute="Error" lineEndContext="#pop#pop" fallthrough="true" fallthroughContext="NumericSuffixError">
        <AnyChar attribute="Standard Suffix" context="NumericSuffixError" String="fFlL" />
      </context>

      <context name="NumericSuffixError" attribute="Error" lineEndContext="#pop#pop#pop" fallthrough="true" fallthroughContext="#pop#pop#pop">
        <RegExpr attribute="Error" context="#pop#pop#pop" String="\.[_0-9A-Za-z]*|[_0-9A-Za-z]+" />
      </context>
    </contexts>
    <itemDatas>
			<itemData name="Normal Text"  defStyleNum="dsNormal" spellChecking="false"/>
      <itemData name="Control Flow" defStyleNum="dsControlFlow" spellChecking="false"/>
      <itemData name="Keyword"      defStyleNum="dsKeyword" spellChecking="false"/>
      <itemData name="Data Type"    defStyleNum="dsDataType" spellChecking="false"/>
      <itemData name="Float"      defStyleNum="dsFloat" spellChecking="false"/>
      <itemData name="int"      defStyleNum="dsDecVal" spellChecking="false"/>
      <itemData name="Standard Suffix" defStyleNum="dsBuiltIn" spellChecking="false" />
      <itemData name="Char"         defStyleNum="dsChar" spellChecking="false"/>
      <itemData name="String"       defStyleNum="dsString"/>
      <itemData name="String Char"  defStyleNum="dsSpecialChar"/>
      <itemData name="Comment"      defStyleNum="dsComment"/>
      <itemData name="Symbol"       defStyleNum="dsOperator" spellChecking="false"/>
      <itemData name="Preprocessor" defStyleNum="dsPreprocessor" spellChecking="false"/>
      <itemData name="Prep. Lib"    defStyleNum="dsImport" spellChecking="false"/>
      <itemData name="Region Marker" defStyleNum="dsRegionMarker" spellChecking="false"/>
    </itemDatas>
  </highlighting>
  <general>
    <comments>
      <comment name="singleLine" start="#" position="afterwhitespace"/>
    </comments>
		<keywords casesensitive="1" additionalDeliminator="#'"/>
  </general>
</language>
<!-- kate: replace-tabs on; tab-width 2; indent-width 2; -->
		"""
		return parte3