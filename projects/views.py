from django.shortcuts import get_object_or_404, render_to_response

from models import Project, Release, Document

def release_list(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    release_list = Release.objects.filter(project=project)

    return render_to_response('projects/release_list.html',
        {'project': project,
            'release_list': release_list})

def release_detail(request, project_slug, release_slug):
    project = get_object_or_404(Project, slug=project_slug)
    release = get_object_or_404(Release, project__slug=project_slug, slug=release_slug)

    return render_to_response('projects/release_detail.html',
        {'project': project,
            'release': release})

def document_list(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    document_list = Document.objects.filter(project=project)

    return render_to_response('projects/document_list.html',
        {'project': project,
            'document_list': document_list})

def document_detail(request, project_slug, document_slug, revision):
    project = get_object_or_404(Project, slug=project_slug)
    document = get_object_or_404(Document, project__slug=project_slug, slug=document_slug,
        revision=revision)
    documents = Document.objects.filter(project__slug=project_slug,
        slug=document_slug).exclude(id=document.id)

    return render_to_response('projects/document_detail.html',
        {'project': project,
            'document': document,
            'document_list': document_list})
