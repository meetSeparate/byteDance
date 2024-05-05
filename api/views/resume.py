from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Resume, WorkInfo, ProjectInfo


class ResumeView(APIView):
    def post(self, request):
        res = {
            'code': 200,
            'msg': 'success',
            'data': {}
        }

        def format_date(date_list):
            return f'{date_list[0]}~{date_list[1]}'

        userid = request.data.get('userid')
        name = request.data.get('name')
        phone = request.data.get('phone')
        email = request.data.get('email')

        school = request.data.get('school')
        degree = request.data.get('degree')
        profession = request.data.get('profession')
        duration = request.data.get('duration')

        work_info_form_list = request.data.get('workInfoFormList')
        internship_form_list = request.data.get('internshipFormList')
        project_form_list = request.data.get('projectFormList')
        resume_query = Resume.objects.filter(user_id=userid)
        if not resume_query.first():
            resume = Resume.objects.create(
                name=name, phone=phone, email=email, school=school, degree=degree, profession=profession,
                duration=format_date(duration), user_id=userid
            )
            for work_info in work_info_form_list:
                work = WorkInfo.objects.create(
                    company=work_info['company'],
                    position=work_info['position'],
                    duration=format_date(work_info['company']),
                    description=work_info['description']
                )
                resume.work_info.add(work.nid)

            for internship_info in internship_form_list:
                work = WorkInfo.objects.create(
                    company=internship_info['company'],
                    position=internship_info['position'],
                    duration=format_date(internship_info['company']),
                    description=internship_info['description'],
                    types='实习'
                )
                resume.work_info.add(work.nid)

            for project__info in project_form_list:
                project = ProjectInfo.objects.create(
                    title=project__info['title'],
                    role=project__info['role'],
                    duration=format_date(project__info['duration']),
                    link=project__info['link'],
                    description=project__info['description'],
                )
                resume.project_info.add(project.nid)
        else:
            resume_query.update(
                name=name, phone=phone, email=email, school=school, degree=degree, profession=profession,
                duration=format_date(duration), user_id=userid
            )
            for work_info in work_info_form_list:
                if not work_info.get('nid'):
                    work = WorkInfo.objects.create(
                        company=work_info['company'],
                        position=work_info['position'],
                        duration=format_date(work_info['duration']),
                        description=work_info['description']
                    )
                    resume_query.first().work_info.add(work.nid)
                else:
                    flag_query = WorkInfo.objects.filter(nid=work_info['nid'])
                    flag_query.update(
                        company=work_info['company'],
                        position=work_info['position'],
                        duration=format_date(work_info['duration']),
                        description=work_info['description']
                    )

            for internship_info in internship_form_list:
                if not internship_info.get('nid'):
                    work = WorkInfo.objects.create(
                        company=internship_info['company'],
                        position=internship_info['position'],
                        duration=format_date(internship_info['duration']),
                        description=internship_info['description'],
                        types='实习'
                    )
                    resume_query.first().work_info.add(work.nid)
                else:
                    flag_query = WorkInfo.objects.filter(nid=internship_info['nid'])
                    flag_query.update(
                        company=internship_info['company'],
                        position=internship_info['position'],
                        duration=format_date(internship_info['duration']),
                        description=internship_info['description']
                    )

            for project_info in project_form_list:

                if not project_info.get('nid'):
                    project = ProjectInfo.objects.create(
                        title=project_info['title'],
                        role=project_info['role'],
                        duration=format_date(project_info['duration']),
                        link=project_info['link'],
                        description=project_info['description'],
                    )
                    resume_query.first().project_info.add(project.nid)
                else:
                    flag_query = ProjectInfo.objects.filter(nid=project_info['nid'])
                    flag_query.update(
                        title=project_info['title'],
                        role=project_info['role'],
                        duration=format_date(project_info['duration']),
                        link=project_info['link'],
                        description=project_info['description'],
                    )
        return Response(res)

    def get(self, request):
        res = {
            'code': 200,
            'msg': 'success',
            'data': {}
        }

        userid = request.GET.get('userid')
        resume = Resume.objects.filter(user_id=userid).first()
        if resume:
            work_info_list = resume.work_info.all()
            project_info_list = resume.project_info.all()
            res['data'] = {
                'name': resume.name,
                'phone': resume.phone,
                'email': resume.email,
                'school': resume.school,
                'degree': resume.degree,
                'profession': resume.profession,
                'duration': resume.duration.split('~'),
                'workList': [],
                'projectList': [],
                'change_date': str(resume.change_date)[:16]
            }
            for work in work_info_list:
                res['data']['workList'].append({
                    'nid': work.nid,
                    'company': work.company,
                    'position': work.position,
                    'duration': work.duration.split('~'),
                    'description': work.description,
                    'types': work.types,
                })

            for project in project_info_list:
                res['data']['projectList'].append({
                    'nid': project.nid,
                    'title': project.title,
                    'role': project.role,
                    'duration': project.duration.split('~'),
                    'link': project.link,
                    'description': project.description,
                })
        return Response(res)
