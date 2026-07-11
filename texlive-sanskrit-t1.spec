%global tl_name sanskrit-t1
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Type 1 version of skt fonts for Sanskrit
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/ps-type1/sanskrit
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sanskrit-t1.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sanskrit-t1.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The sanskrit-t1 font package provides Type 1 version of Charles Wikner's
skt font series for the Sanskrit language.

