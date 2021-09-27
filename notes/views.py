from django.shortcuts import render, redirect
from .models import Note, Tag
from .form import NoteForm

def index(request):
    if request.method == 'POST':
        metodo = request.POST.get('metodo')
        if metodo == "post":
            title = request.POST.get('titulo')
            content = request.POST.get('detalhes')
            tag = request.POST.get('tag')
            new_tag = Tag(name=tag)         
            for tag in Tag.objects.all():
                if new_tag.name == tag.name:
                    note = Note(title= title, content = content, tag=tag)
                    note.save()
                    return redirect('index')
            new_tag.save()
            note = Note(title= title, content = content, tag=new_tag)
            note.save() 

        elif metodo == "delete":
            id = request.POST.get('id')
            note = Note.objects.get(id=id)
            note.delete()

        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def update_card(request, id):
    note = Note.objects.get(id=id)
    form = NoteForm(request.POST or None, instance=note)

    if form.is_valid():
        form.save()
        return redirect('index')

    
    return render(request, 'notes/note-form.html', {'form': form, 'note': note})
