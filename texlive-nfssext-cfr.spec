%global tl_name nfssext-cfr
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Extensions to the LaTeX NFSS
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nfssext-cfr
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nfssext-cfr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nfssext-cfr.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nfssext-cfr.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is a development of nfssext.sty, distributed with the
examples for the font installation guide. The package has been developed
for use in packages such as cfr-lm and venturisadf,

