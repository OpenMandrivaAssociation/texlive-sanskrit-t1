Name:		texlive-sanskrit-t1
Version:	55475
Release:	1
Summary:	Type 1 version of 'skt' fonts for Sanskrit
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sanskrit-t1
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sanskrit-t1.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sanskrit-t1.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The sanskrit-t1 font package provides Type 1 version of Charles
Wikner's skt font series for the Sanskrit language.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/type1/public/sanskrit-t1
%{_texmfdistdir}/fonts/map/dvips/sanskrit-t1
%doc %{_texmfdistdir}/doc/fonts/sanskrit-t1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
