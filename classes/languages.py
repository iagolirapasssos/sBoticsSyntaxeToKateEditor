class Linguagens:
	def __init__(self, linguagem, idioma):
		self.name = linguagem
		self.age = idioma

	def reduc_ptbr_parte1(self):
		parte1="""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE language
	SYSTEM 'language.dtd' [

	<!ENTITY symbols "(?:@{1,2}|\$)?[a-zA-Z_][a-zA-Z0-9_]*[=?!]?">
]>
<!--
	REDUC PT-BR syntax highlighting definition for Kate.

	Copyright (C) 2021  by Francisco Iago Lira Passos (iagolirapassos@gmail.com)
	Copyright (C) 2021  by Vinicios Lugli (vinicioslugli@gmail.com)

	This library is free software; you can redistribute it and/or
	modify it under the terms of the GNU Library General Public
	License as published by the Free Software Foundation; either
	version 2 of the License, or (at your option) any later version.
	This library is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
	Library General Public License for more details.
	You should have received a copy of the GNU Library General Public
	License along with this library; if not, write to the
	Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
	Boston, MA  02110-1301, USA.
-->
<!-- Hold the "language" opening tag on a single line, as mentioned in "language.dtd". -->
<language author="Francisco Iago Lira Passos (iagolirapassos@gmail.com), Vinicios Lugli (vinicioslugli@gmail.com)"
					extensions="*.sBotics"
					indenter=""
					kateversion="5.79"
					license="LGPLv2+"
					mimetype="text/plain"
					name="R-EDUC"
					section="Sources"
					style=""
					version="11">
<highlighting>
<list name="control-flow">
	<item>farei</item>
	<item>enquanto</item>
	<item>repita</item>
	<item>vezes</item>
	<item>de</item>
	<item>ate</item>
	<item>passo</item>
	<item>teste</item>
	<item>caso</item>
	<item>outros</item>
	<item>se</item>
	<item>entao</item>
	<item>senao</item>
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
			<!-- "shebang" line -->
			<RegExpr String="^#!\/.*" attribute="Keyword" column="0" context="#stay"/>

			<!-- Defined words -->
			<keyword String="keywords" attribute="Keyword" context="#stay"/>
			<keyword String="control-flow" attribute="Control Flow" context="#stay"/>
			<keyword String="types" attribute="Types" context="#stay"/>

			<!-- definições que foram comentadas
			<keyword String="mixin-macros" attribute="Mixin macros" context="#stay"/>
			<keyword String="definitions" attribute="Definition" context="#stay"/>
			<keyword String="pseudo-variables" attribute="Pseudo variable" context="#stay"/>
			-->

			<!-- special-character globals -->
			<RegExpr String="\\b[_A-Z]+[A-Z_0-9]+\\b" attribute="Global Constant" context="#stay"/>

			<!-- Generally a module or class name like "File", "MyModule_1", .. -->
			<RegExpr String="\\b[A-Z]+_*(?:[0-9]|[a-z])[_a-zA-Z0-9]*\\b" attribute="Constant" context="#stay"/>

			<!-- Numeric values. Note that we have to allow underscores between two digits (thus the creepy regular expressions). -->
			<RegExpr String="\\b\-?0[xX](?:[0-9a-fA-F]|_[0-9a-fA-F])+" attribute="Hex" context="#stay"/>
			<RegExpr String="\\b\-?0[bB](?:[01]|_[01])+" attribute="Bin" context="#stay"/>
			<RegExpr String="\\b\-?0[1-7](?:[0-7]|_[0-7])*" attribute="Octal" context="#stay"/>
			<RegExpr String="\\b\-?[0-9](?:[0-9]|_[0-9])*\.[0-9](?:[0-9]|_[0-9])*(?:[eE]\-?[1-9](?:[0-9]|_[0-9])*(?:\.[0-9]*)?)?" attribute="Float" context="#stay"/>
			<RegExpr String="\\b\-?[1-9](?:[0-9]|_[0-9])*\\b" attribute="Dec" context="#stay"/>
			<Int attribute="Dec" context="#stay"/>
			<HlCChar attribute="Char" context="#stay"/>
			<DetectChar attribute="Operator" char="." context="#stay"/>
			<Detect2Chars attribute="Operator" char="&amp;" char1="&amp;" context="#stay"/>
			<Detect2Chars attribute="Operator" char="|" char1="|" context="#stay"/>
			<!-- \s!|/=\s is regexp hack -->
			<RegExpr String="\s[\?\:\%]\s|[|&amp;&lt;&gt;\^\+*~\-=/]+|\s!|/=\s" attribute="Operator" context="#stay"/>
			<Detect2Chars char="%" char1="=" attribute="Operator" context="#stay"/>
			<RegExpr String=":&symbols;|\\b&symbols;:|:\[\]=?" attribute="Symbol" context="#stay"/>
			<RegExpr String="@(?:module)?doc\s+&quot;&quot;&quot;" attribute="Attribute" context="Documentation"/>
			<StringDetect String="&quot;&quot;&quot;" attribute="String" context="Triple Quoted String"/>
			<DetectChar attribute="String" char="&quot;" context="Quoted String"/>
			<DetectChar attribute="Raw String" char="'" context="Apostrophed String"/>
			<Detect2Chars char="?" char1="#" attribute="Normal Text" context="#stay"/>
			<DetectChar attribute="Comment" char="#" context="General Comment"/>
			<AnyChar attribute="Delimiter" String="[]" context="#stay"/>
			<RegExpr String="@[a-zA-Z_0-9]+" attribute="Attribute" context="#stay"/>
			<!-- handle the different regular expression formats -->
			<DetectChar attribute="Normal Text" char=")" context="#stay"/>
			<DetectIdentifier attribute="Normal Text" context="#stay"/>
		</context>
		<context attribute="DocComment" lineEndContext="#stay" name="Documentation">
			<StringDetect String="&quot;&quot;&quot;" attribute="Attribute" context="#pop"/>
			<RegExpr attribute="MarkdownHead" String="^\s*#+\s.*[#]?$" column="0"/>
			<RegExpr attribute="MarkdownBullet" String="^\s*[\*\+\-]\s" column="0"/>
			<RegExpr attribute="MarkdownNumlist" String="^\s*[\d]+\.\s" column="0"/>
			<RegExpr attribute="MarkdownCode" context="Markdown Code" String="^\s*\`\`\`\s*$" column="0"/>
			<DetectSpaces />
			<IncludeRules context="Normal Text##Markdown"/>
		</context>
		<context attribute="String" lineEndContext="#stay" name="Triple Quoted String">
			<StringDetect String="&quot;&quot;&quot;" attribute="String" context="#pop"/>
		</context>
		<context attribute="String" lineEndContext="#stay" name="Quoted String">
			<Detect2Chars char="\\" char1="\\" attribute="String" context="#stay"/>
			<Detect2Chars char="\\" char1="&quot;" attribute="String" context="#stay"/>
			<RegExpr String="#@{1,2}" attribute="Substitution" context="Short Subst"/>
			<Detect2Chars attribute="Substitution" char="#" char1="{" context="Subst"/>
			<DetectChar attribute="String" char="&quot;" context="#pop"/>
		</context>
		<context attribute="Raw String" lineEndContext="#stay" name="Apostrophed String">
			<Detect2Chars char="\\" char1="\\" attribute="String" context="#stay"/>
			<Detect2Chars char="\\" char1="'" attribute="String" context="#stay"/>
			<DetectChar attribute="Raw String" char="'" context="#pop"/>
		</context>
		<!-- Substitutions can be nested -->
		<context attribute="Normal Text" lineEndContext="#stay" name="Subst">
			<DetectChar attribute="Substitution" char="}" context="#pop"/>
			<!-- Highlight substitution as code. -->
			<IncludeRules context="Normal"/>
		</context>
		<context attribute="Substitution" lineEndContext="#pop" name="Short Subst">
			<!-- Check for e.g.: "#@var#@@xy" -->
			<RegExpr String="#@{1,2}" attribute="Substitution" context="#stay"/>
			<RegExpr String="\w(?!\w)" attribute="Substitution" context="#pop"/>
		</context>
		<context attribute="Comment" lineEndContext="#pop" name="General Comment">
			<DetectSpaces />
			<IncludeRules context="##Comments"/>
		</context>
		<context attribute="MarkdownCode" lineEndContext="#stay" name="Markdown Code">
			<RegExpr String="^\s*```\s*$" attribute="MarkdownCode" context="#pop" column="0"/>
		</context>
	</contexts>
	<itemDatas>
		<itemData name="Global Constant" defStyleNum="dsConstant"/>
		<itemData name="Constant" defStyleNum="dsConstant"/>
		<itemData defStyleNum="dsNormal" name="Normal Text"/>
		<itemData defStyleNum="dsKeyword" name="Keyword"/>
		<itemData defStyleNum="dsControlFlow" name="Control Flow"/>
		<itemData defStyleNum="dsDataType" name="Types"/>
		<itemData defStyleNum="dsDecVal" name="Dec"/>
		<itemData defStyleNum="dsFloat" name="Float"/>
		<itemData defStyleNum="dsChar" name="Char"/>
		<itemData defStyleNum="dsBaseN" name="Octal"/>
		<itemData defStyleNum="dsBaseN" name="Hex"/>
		<itemData defStyleNum="dsBaseN" name="Bin"/>
		<itemData defStyleNum="dsVariable" name="Symbol"/>
		<itemData defStyleNum="dsString" name="String"/>
		<itemData defStyleNum="dsVerbatimString" name="Raw String"/>
		<itemData defStyleNum="dsOthers" name="Substitution"/>
		<itemData defStyleNum="dsOthers" name="Attribute"/>
		<itemData defStyleNum="dsComment" name="Comment"/>
		<itemData defStyleNum="dsComment" name="DocComment"/>
		<!-- use these to mark errors and alerts things -->
		<itemData color="#FF9FEC" defStyleNum="dsNormal" name="Delimiter"/>
		<itemData defStyleNum="dsOperator" name="Operator"/>
		<itemData name="MarkdownHead" defStyleNum="dsFunction" bold="true"/>
		<itemData name="MarkdownBullet" defStyleNum="dsFunction"/>
		<itemData name="MarkdownNumlist" defStyleNum="dsFunction"/>
		<itemData name="MarkdownCode" defStyleNum="dsFunction"/>
	</itemDatas>
</highlighting>
<general>
	<comments>
		<comment name="singleLine" start="#"/>
	</comments>
	<keywords casesensitive="1" weakDeliminator="!?"/>
</general>
</language>
<!-- kate: replace-tabs on; tab-width 2; indent-width 2; -->
		"""
		return parte3

	def reduc_en_parte1(self):
		parte1="""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE language
	SYSTEM 'language.dtd' [

	<!ENTITY symbols "(?:@{1,2}|\$)?[a-zA-Z_][a-zA-Z0-9_]*[=?!]?">
]>
<!--
	REDUC PT-BR syntax highlighting definition for Kate.

	Copyright (C) 2021  by Francisco Iago Lira Passos (iagolirapassos@gmail.com)
	Copyright (C) 2021  by Vinicios Lugli (vinicioslugli@gmail.com)

	This library is free software; you can redistribute it and/or
	modify it under the terms of the GNU Library General Public
	License as published by the Free Software Foundation; either
	version 2 of the License, or (at your option) any later version.
	This library is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
	Library General Public License for more details.
	You should have received a copy of the GNU Library General Public
	License along with this library; if not, write to the
	Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
	Boston, MA  02110-1301, USA.
-->
<!-- Hold the "language" opening tag on a single line, as mentioned in "language.dtd". -->
<language author="Francisco Iago Lira Passos (iagolirapassos@gmail.com), Vinicios Lugli (vinicioslugli@gmail.com)"
					extensions="*.sBotics;*.reduc"
					indenter=""
					kateversion="5.79"
					license="LGPLv2+"
					mimetype="text/plain"
					name="R-EDUC"
					section="Sources"
					style=""
					version="11">
<highlighting>
<list name="control-flow">
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
	<item>case</item>
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
	<item>number</item>
	<item>text</item>
	<item>boolean</item>
</list>

<contexts>
	<context attribute="Normal Text" lineEndContext="#stay" name="Normal">
		<!-- "shebang" line -->
		<RegExpr String="^#!\/.*" attribute="Keyword" column="0" context="#stay"/>

		<!-- Defined words -->
		<keyword String="keywords" attribute="Keyword" context="#stay"/>
		<keyword String="control-flow" attribute="Control Flow" context="#stay"/>
		<keyword String="types" attribute="Types" context="#stay"/>

		<!-- definições que foram comentadas
		<keyword String="mixin-macros" attribute="Mixin macros" context="#stay"/>
		<keyword String="definitions" attribute="Definition" context="#stay"/>
		<keyword String="pseudo-variables" attribute="Pseudo variable" context="#stay"/>
		-->

		<!-- special-character globals -->
		<RegExpr String="\\b[_A-Z]+[A-Z_0-9]+\\b" attribute="Global Constant" context="#stay"/>

		<!-- Generally a module or class name like "File", "MyModule_1", .. -->
		<RegExpr String="\\b[A-Z]+_*(?:[0-9]|[a-z])[_a-zA-Z0-9]*\\b" attribute="Constant" context="#stay"/>

		<!-- Numeric values. Note that we have to allow underscores between two digits (thus the creepy regular expressions). -->
		<RegExpr String="\\b\-?0[xX](?:[0-9a-fA-F]|_[0-9a-fA-F])+" attribute="Hex" context="#stay"/>
		<RegExpr String="\\b\-?0[bB](?:[01]|_[01])+" attribute="Bin" context="#stay"/>
		<RegExpr String="\\b\-?0[1-7](?:[0-7]|_[0-7])*" attribute="Octal" context="#stay"/>
		<RegExpr String="\\b\-?[0-9](?:[0-9]|_[0-9])*\.[0-9](?:[0-9]|_[0-9])*(?:[eE]\-?[1-9](?:[0-9]|_[0-9])*(?:\.[0-9]*)?)?" attribute="Float" context="#stay"/>
		<RegExpr String="\\b\-?[1-9](?:[0-9]|_[0-9])*\\b" attribute="Dec" context="#stay"/>
		<Int attribute="Dec" context="#stay"/>
		<HlCChar attribute="Char" context="#stay"/>
		<DetectChar attribute="Operator" char="." context="#stay"/>
		<Detect2Chars attribute="Operator" char="&amp;" char1="&amp;" context="#stay"/>
		<Detect2Chars attribute="Operator" char="|" char1="|" context="#stay"/>
		<!-- \s!|/=\s is regexp hack -->
		<RegExpr String="\s[\?\:\%]\s|[|&amp;&lt;&gt;\^\+*~\-=/]+|\s!|/=\s" attribute="Operator" context="#stay"/>
		<Detect2Chars char="%" char1="=" attribute="Operator" context="#stay"/>
		<RegExpr String=":&symbols;|\\b&symbols;:|:\[\]=?" attribute="Symbol" context="#stay"/>
		<RegExpr String="@(?:module)?doc\s+&quot;&quot;&quot;" attribute="Attribute" context="Documentation"/>
		<StringDetect String="&quot;&quot;&quot;" attribute="String" context="Triple Quoted String"/>
		<DetectChar attribute="String" char="&quot;" context="Quoted String"/>
		<DetectChar attribute="Raw String" char="'" context="Apostrophed String"/>
		<Detect2Chars char="?" char1="#" attribute="Normal Text" context="#stay"/>
		<DetectChar attribute="Comment" char="#" context="General Comment"/>
		<AnyChar attribute="Delimiter" String="[]" context="#stay"/>
		<RegExpr String="@[a-zA-Z_0-9]+" attribute="Attribute" context="#stay"/>
		<!-- handle the different regular expression formats -->
		<DetectChar attribute="Normal Text" char=")" context="#stay"/>
		<DetectIdentifier attribute="Normal Text" context="#stay"/>
	</context>
	<context attribute="DocComment" lineEndContext="#stay" name="Documentation">
		<StringDetect String="&quot;&quot;&quot;" attribute="Attribute" context="#pop"/>
		<RegExpr attribute="MarkdownHead" String="^\s*#+\s.*[#]?$" column="0"/>
		<RegExpr attribute="MarkdownBullet" String="^\s*[\*\+\-]\s" column="0"/>
		<RegExpr attribute="MarkdownNumlist" String="^\s*[\d]+\.\s" column="0"/>
		<RegExpr attribute="MarkdownCode" context="Markdown Code" String="^\s*\`\`\`\s*$" column="0"/>
		<DetectSpaces />
		<IncludeRules context="Normal Text##Markdown"/>
	</context>
	<context attribute="String" lineEndContext="#stay" name="Triple Quoted String">
		<StringDetect String="&quot;&quot;&quot;" attribute="String" context="#pop"/>
	</context>
	<context attribute="String" lineEndContext="#stay" name="Quoted String">
		<Detect2Chars char="\\" char1="\\" attribute="String" context="#stay"/>
		<Detect2Chars char="\\" char1="&quot;" attribute="String" context="#stay"/>
		<RegExpr String="#@{1,2}" attribute="Substitution" context="Short Subst"/>
		<Detect2Chars attribute="Substitution" char="#" char1="{" context="Subst"/>
		<DetectChar attribute="String" char="&quot;" context="#pop"/>
	</context>
	<context attribute="Raw String" lineEndContext="#stay" name="Apostrophed String">
		<Detect2Chars char="\\" char1="\\" attribute="String" context="#stay"/>
		<Detect2Chars char="\\" char1="'" attribute="String" context="#stay"/>
		<DetectChar attribute="Raw String" char="'" context="#pop"/>
	</context>
	<!-- Substitutions can be nested -->
	<context attribute="Normal Text" lineEndContext="#stay" name="Subst">
		<DetectChar attribute="Substitution" char="}" context="#pop"/>
		<!-- Highlight substitution as code. -->
		<IncludeRules context="Normal"/>
	</context>
	<context attribute="Substitution" lineEndContext="#pop" name="Short Subst">
		<!-- Check for e.g.: "#@var#@@xy" -->
		<RegExpr String="#@{1,2}" attribute="Substitution" context="#stay"/>
		<RegExpr String="\w(?!\w)" attribute="Substitution" context="#pop"/>
	</context>
	<context attribute="Comment" lineEndContext="#pop" name="General Comment">
		<DetectSpaces />
		<IncludeRules context="##Comments"/>
	</context>
	<context attribute="MarkdownCode" lineEndContext="#stay" name="Markdown Code">
		<RegExpr String="^\s*```\s*$" attribute="MarkdownCode" context="#pop" column="0"/>
	</context>
</contexts>
<itemDatas>
	<itemData name="Global Constant" defStyleNum="dsConstant"/>
	<itemData name="Constant" defStyleNum="dsConstant"/>
	<itemData defStyleNum="dsNormal" name="Normal Text"/>
	<itemData defStyleNum="dsKeyword" name="Keyword"/>
	<itemData defStyleNum="dsControlFlow" name="Control Flow"/>
	<itemData defStyleNum="dsDataType" name="Types"/>
	<itemData defStyleNum="dsDecVal" name="Dec"/>
	<itemData defStyleNum="dsFloat" name="Float"/>
	<itemData defStyleNum="dsChar" name="Char"/>
	<itemData defStyleNum="dsBaseN" name="Octal"/>
	<itemData defStyleNum="dsBaseN" name="Hex"/>
	<itemData defStyleNum="dsBaseN" name="Bin"/>
	<itemData defStyleNum="dsVariable" name="Symbol"/>
	<itemData defStyleNum="dsString" name="String"/>
	<itemData defStyleNum="dsVerbatimString" name="Raw String"/>
	<itemData defStyleNum="dsOthers" name="Substitution"/>
	<itemData defStyleNum="dsOthers" name="Attribute"/>
	<itemData defStyleNum="dsComment" name="Comment"/>
	<itemData defStyleNum="dsComment" name="DocComment"/>
	<!-- use these to mark errors and alerts things -->
	<itemData color="#FF9FEC" defStyleNum="dsNormal" name="Delimiter"/>
	<itemData defStyleNum="dsOperator" name="Operator"/>
	<itemData name="MarkdownHead" defStyleNum="dsFunction" bold="true"/>
	<itemData name="MarkdownBullet" defStyleNum="dsFunction"/>
	<itemData name="MarkdownNumlist" defStyleNum="dsFunction"/>
	<itemData name="MarkdownCode" defStyleNum="dsFunction"/>
</itemDatas>
</highlighting>
<general>
	<comments>
		<comment name="singleLine" start="#"/>
	</comments>
	<keywords casesensitive="1" weakDeliminator="!?"/>
</general>
</language>
<!-- kate: replace-tabs on; tab-width 2; indent-width 2; -->
		"""
		return parte3